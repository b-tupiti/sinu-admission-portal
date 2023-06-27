from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from .models import Application, Document, ApplicationToken, ApplicationState, CurrentSection
from courses.models.course import Course
from django.shortcuts import redirect
from django.urls import reverse
from users.models.user import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from users.utils import create_applicant_account
from admission.utils import create_new_admission_application_for_user, save_personal_details, save_sponsor_details, get_course_from_code
from django.http import Http404

def create_new_admission(request):
    
    if request.method == 'GET':
        
        if request.GET.get('course_code') is None:
            return redirect('find-course')
        
        course = get_course_from_code(request)
        context = {'course':course}
        
        return render(request, 'application/create-new-admission.html', context)
    
    
    elif request.method == 'POST':     
        
        email, password = create_applicant_account(request)
        user = authenticate(request, email=email, password=password)
        
        course_code = request.POST.get('course_code')
        course = Course.objects.get(code=course_code)
        
        login(request, user)
        application = create_new_admission_application_for_user(user, course)
        
        return redirect(reverse('personal-details',args=[application.id]))
  

    



@login_required(login_url='login')
def personal_details(request,pk):
    
    try:
        application = get_object_or_404(Application, id=pk)
        application.current_section = CurrentSection.PERSONAL_DETAILS
        application.save()
    except Http404:
        return render(request,'admission/application_404.html')
    
    if not application.owner == request.user:
        return render(request,'admission/application_403.html')
    
    if application.application_state == ApplicationState.SUBMITTED:
        return redirect('dashboard')
    
    if request.method == 'POST':
        save_personal_details(request, application)
        
        if 'save_and_exit' in request.POST:
            return redirect('application-saved')
        else:
            return redirect(reverse('sponsor-details',args=[application.id]))
   
    context = {
        'application': application
    }
    
    return render(request, 'application/personal-details.html', context)




@login_required(login_url='login')
def sponsor_details(request, pk):
    
    try:
        application = get_object_or_404(Application, id=pk)
        application.current_section = CurrentSection.SPONSOR_DETAILS
        application.save()
    except Http404:
        return render(request,'admission/application_404.html')
    
    if not application.owner == request.user:
        return render(request,'admission/application_403.html')
    
    if request.method == 'POST':
        save_sponsor_details(request, application)
        
        if 'save_and_exit' in request.POST:
            return redirect('application-saved')
        else:
            return redirect(reverse('education-background',args=[application.id]))
        
    context = {
        'application': application
    }
        
    return render(request, 'application/sponsor-details.html', context)

@login_required(login_url='login')
def education_background(request, pk):
    
    try:
        application = get_object_or_404(Application, id=pk)
        application.current_section = CurrentSection.EDUCATION_BACKGROUND
        application.save()
    except Http404:
        return render(request,'admission/application_404.html')
    
    if not application.owner == request.user:
        return render(request,'admission/application_403.html')
    
    if request.method == 'POST':
        if 'save_and_exit' in request.POST:
            return redirect('application-saved')
        else:
            return redirect(reverse('employment-history',args=[application.id]))
    
    context = {'application':application}
    return render(request, 'application/education-background.html',context)



@login_required(login_url='login')
def employment_history(request, pk):
    
    try:
        application = get_object_or_404(Application, id=pk)
        application.current_section = CurrentSection.EMPLOYMENT_HISTORY
        application.save()
    except Http404:
        return render(request,'admission/application_404.html')
    
    if not application.owner == request.user:
        return render(request,'admission/application_403.html')
    
    if request.method == 'POST':
        if 'save_and_exit' in request.POST:
            return redirect('application-saved')
        else:
            return redirect(reverse('declaration',args=[application.id]))
    
    context = {'application':application}
    return render(request, 'application/employment-history.html', context)




@login_required(login_url='login')
def declaration(request, pk):
    
    try:
        application = get_object_or_404(Application, id=pk)
        application.current_section = CurrentSection.DECLARATION
        application.save()
    except Http404:
        return render(request,'admission/application_404.html')
    
    if not application.owner == request.user:
        return render(request,'admission/application_403.html')
    
    if request.method == 'POST':
        if 'save_and_exit' in request.POST:
            return redirect('application-saved')
        else:
            application.application_state = ApplicationState.SUBMITTED
            application.is_declared = True
            application.save()
            return redirect('dashboard')
        
    context = {'application':application}
    return render(request, 'application/declaration.html', context)



@login_required(login_url='login')
def application_saved(request):
    return render(request, 'application/application-saved.html')











def my_admissions(request):
    return render(request, 'application/my-admissions.html')



# def submission_form(request):
#     """
#     displays a form for the user to submit an application
#     """
#     is_submitted = False
    
#     DocumentFormSet = formset_factory(DocumentForm, extra=1)
#     document_formset = DocumentFormSet(prefix='document')
#     application_form = ApplicationForm()
    
#     if request.method == 'POST':
        
#         # get photos and all documents
#         photo = request.FILES['photo']
#         doc_keys = [key for key in request.FILES if key != 'photo']
#         documents = [request.FILES[key] for key in doc_keys]
        
#         application_form = ApplicationForm(request.POST, {'photo': photo})
        
#         if application_form.is_valid():
#             application = application_form.save()
#             for document in documents:
#                 Document.objects.create(file=document,application=application)

#         is_submitted = True
    
#     context = {
#         'application_form':application_form, 
#         'document_formset': document_formset,
#         'is_submitted': is_submitted,
#     }
    
#     return render(request, 'mbasubmission/right-section/template.html',context)


def upload_deposit_slip(request):
    
    token = request.GET.get('token')
    context = {}
    
    try:
        token = ApplicationToken.objects.get(id=token)
        application = Application.objects.get(id=token.application.id)
        context['application'] = application
    except ApplicationToken.DoesNotExist:
        pass
    
    return render(request, 'deposit/upload_deposit.html', context)
    