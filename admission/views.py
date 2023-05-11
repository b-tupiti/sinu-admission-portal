from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from .models import Application, Document, ApplicationToken
from courses.models.course import Course
from django.shortcuts import redirect
from users.models.user import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from users.utils import create_applicant_account
from admission.utils import create_new_admission_application_for_user, save_personal_details, save_sponsor_details

    
def create_new_admission(request):
    
    context = {}
    
    if request.GET.get('course_code') is None:
        return redirect('find-course')
    
    course_code = request.GET.get('course_code')
    course = Course.objects.get(code=course_code)
    context['course'] = course
    

    if request.method == 'POST':     
        
        email, password = create_applicant_account(request)
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            application = create_new_admission_application_for_user(user, course)
            request.session['application_id'] = application.id
            return redirect('personal-details')
        else:
            messages.error(request,'cannot create new admission application')

    return render(request, 'application/create-new-admission.html', context)



@login_required(login_url='login')
def personal_details(request):

    id = request.session.get('application_id')
    application = Application.objects.get(id=id)
    
    if request.method == 'POST':
        save_personal_details(request, application)
        
        if 'save_and_exit' in request.POST:
            return redirect('application-saved')
        else:
            return redirect('sponsor-details')
   
    context = {
        'application': application
    }
    
    return render(request, 'application/personal-details.html', context)





def sponsor_details(request):
    
    id = request.session.get('application_id')
    application = Application.objects.get(id=id)
    
    if request.method == 'POST':
        save_sponsor_details(request, application)
        
        if 'save_and_exit' in request.POST:
            return redirect('application-saved')
        else:
            return redirect('education-background')
        
    context = {
        'application': application
    }
        
    return render(request, 'application/sponsor-details.html', context)








def application_saved(request):
    return render(request, 'application/application-saved.html')





def education_background(request):
    return render(request, 'application/education-background.html')

def employment_history(request):
    return render(request, 'application/employment-history.html')

def declaration(request):
    return render(request, 'application/declaration.html')

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
    