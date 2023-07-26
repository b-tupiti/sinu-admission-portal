from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models.application import Application, ApplicationState, Section
from courses.models.course import Course
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login
from users.utils import create_applicant_account
from django.http import Http404
from admission.utils import ( 
    create_new_admission_application_for_user, 
    get_course_from_code, 
    update_current_section, 
    change_edit_section, 
    section_icon_clicked, 
    add_documents_to_context,
)




def create_new_application(request):
    
    if request.method == 'GET':
        
        if request.GET.get('course_code') is None:
            return redirect('find-course')
        
        course = get_course_from_code(request)
        context = {'course':course}
        
        return render(request, 'admission/application/create-new-application.html', context)
    
    
    elif request.method == 'POST':     
        
        email, password = create_applicant_account(request)
        user = authenticate(request, email=email, password=password)
        
        course_code = request.POST.get('course_code')
        course = Course.objects.get(code=course_code)
        
        login(request, user)
        application = create_new_admission_application_for_user(user, course)
        
        return redirect(reverse('application',args=[application.id]))
  
  
@login_required(login_url='login')
def application(request, pk):
    
    # checks if application exist, else render 404
    try:
        application = get_object_or_404(Application, id=pk)
    except Http404:
        return render(request, 'admission/errors/application_404.html')
    
    # check if client does not own application, else render 403
    if not application.owner == request.user:
        return render(request, 'admission/errors/application_403.html')
    
    # check if application is submitted, if it is, redirect to dashboard 
    if application.application_state == ApplicationState.SUBMITTED:
        return redirect('dashboard')
    
    # handles POST request from the progress bar icons, next button, and submit button
    if request.method == 'POST':
        
        if section_icon_clicked(request):
            application = change_edit_section(request, application)
        
        elif 'save_and_exit' in request.POST:
            application.save()
            return redirect('application-saved', pk=application.id)
        
        elif 'submit_application' in request.POST:
            application.application_state = ApplicationState.SUBMITTED
            application.is_declared = True
            application.save()
            return redirect('dashboard')

        else:   
            application = update_current_section(request, application)
        
        application.save()
    
    context = {
        'application': application
    }
    
    # before returning the application to templates, check which section (edit_section)   
    # will be rendered in the template so that the appropriate document names (if there are any)    
    # for that section will be made available to be rendered.
    # filtering documents to be returned inside the context
    
    if application.edit_section == Section.EDUCATION_BACKGROUND: 
        documents = application.high_school_documents.all()
        context = add_documents_to_context(documents, application, context)
        tertiary_qualifications = application.tertiary_qualifications.all()
        context['tertiary_qualifications'] = tertiary_qualifications
        
    return render(request, 'admission/application/application-form-template.html', context)


@login_required(login_url='login')
def application_saved(request, pk):
    
    try:
        application = get_object_or_404(Application, id=pk)
    except Http404:
        return render(request, 'admission/errors/application_404.html')
    
    if not application.owner == request.user:
        return render(request, 'admission/errors/application_403.html')
    
    if application.application_state == ApplicationState.SUBMITTED:
        return redirect('dashboard')
    
    context = {
        'application': application,
    }
    
    return render(request, 'admission/application/application-saved.html', context)
