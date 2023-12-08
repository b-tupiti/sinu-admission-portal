from urllib.parse import urlparse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models.application import Application, ApplicationStatus, Section
from .models.employment import Employment
from courses.models.course import Course
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login
from users.utils import create_applicant_account
from django.http import Http404, StreamingHttpResponse
from .utils.new_application import create_new_admission_application_for_user
from .utils.request_helpers import (
    is_put_request, 
    param_not_found_or_empty
)
from .utils.application_updates import (
    save_current_section, # should be updating furthest section here
    save_current_section_modified,
    change_current_section, 
    get_tertiary_qualifications, 
    get_hs_qualifications,
    handle_submission,
)
from courses.utils import course_does_not_exist
import zipfile
from io import BytesIO
from django.db.utils import IntegrityError
from django.contrib.auth import logout
from config import settings
from b2sdk.v2 import B2Api
from urllib.parse import urlparse
    
def create_new_application(request):
    """
    This view expects a course_code parameter on a GET request, which will be used
    when a subsequent POST request is made to create a new admission application. 
    
    If this parameter is not present, has an empty value, or the value does not match a Course instance, the user
    will be redirected to the 'search-course' url. The assumption is that we are creating a new application
    for a course, hence it must have existed beforehand.
    """
    
    if request.user.is_authenticated:
        message = 'INFO: You can only submit one application at this time.'
        messages.info(request, message)
        return redirect('dashboard')
    
    if request.method == 'GET':
        course_code = request.GET.get('course_code')
        
        if param_not_found_or_empty(course_code) or course_does_not_exist(course_code):
            return redirect('course-search')
        
        course_details = Course.objects.values('code', 'title', 'campus').get(code=course_code)
        context = {'course_details': course_details}
        
        return render(request, 'admission/application/sections/new_application/new-application.html', context)
    
    elif request.method == 'POST':
        
        course_code = request.POST.get('course_code')
        course = Course.objects.get(code=course_code)
        
        try:     
            email, password = create_applicant_account(request)
        except IntegrityError:
            messages.error(request, 'An account with this email already exists.')
            course_details = Course.objects.values('code', 'title', 'campus').get(code=course_code)
            context = {'course_details': course_details}
            return render(request, 'admission/application/sections/new_application/new-application.html', context)
        
        user = authenticate(request, email=email, password=password)
        

        login(request, user)
        application = create_new_admission_application_for_user(user, course)
        
        return redirect(reverse('application',args=[application.id]))
  

@login_required(login_url='login')
def get_application(request, pk):
    
    # checks if application exist, else render 404
    try:
        application = get_object_or_404(Application, id=pk)
    except Http404:
        return render(request, 'admission/errors/application_404.html')
    
    # check if client does not own application, else render 403
    if not application.owner == request.user:
        return render(request, 'admission/errors/application_403.html')
    
    # check if application is submitted, if it is, redirect to dashboard 
    if application.application_status == ApplicationStatus.PENDING_DEPOSIT_VERIFICATION:
        return redirect('dashboard')
    
    
    
    # handles POST request from the progress bar icons, next button, and submit button
    if request.method == 'POST':
        
        if is_put_request(request):
            application = change_current_section(request, application)
            
        else:
            
            if 'save_and_exit' in request.POST:
                # application = save_current_section(request, application) # this function needs refactoring
                application = save_current_section_modified(request, application)
                return redirect('application-saved', pk=application.id)
            
            elif 'submit_application' in request.POST:
                handle_submission(request, application)
                return redirect('dashboard')

            else:   
                application = save_current_section(request, application)
        
        application.save()
        from django.db import connection
        print(connection.queries)
    
    context = {
        'application': application
    }
    
    
    course_code = application.selected_course.code
    course_details = Course.objects.values('code', 'title', 'campus').get(code=course_code)
    context['course_details'] = course_details
    
    if application.current_section == Section.PERSONAL_DETAILS:
        from .models.application import MaritalStatus, Gender, Title, Constituency, Province
        from django_countries import countries
        context['marital_status'] =  MaritalStatus
        context['genders'] =  Gender
        context['titles'] =  Title
        context['constituencies'] =  Constituency
        context['provinces'] =  Province
        context['countries'] =  countries
        return render(request, 'admission/application/sections/personal_details/pd-base.html', context)
    
    if application.current_section == Section.SPONSOR_DETAILS:
        return render(request, 'admission/application/sections/sponsor_details/sd-base.html', context)
    
    if application.current_section == Section.EDUCATION_BACKGROUND:
        context['hs_qualifications'] = get_hs_qualifications(application)
        context['tertiary_qualifications'] = get_tertiary_qualifications(application)
        return render(request, 'admission/application/sections/education_background/eb-base.html', context)
    
    if application.current_section == Section.EMPLOYMENT_HISTORY:
        context['current_employment'] = Employment.objects.filter(is_current=True, application=application).first()
        context['previous_employments'] = Employment.objects.filter(is_current=False, application=application)
        return render(request, 'admission/application/sections/employment_history/eh-base.html', context)
    
    if application.current_section == Section.DECLARATION:
        return render(request, 'admission/application/sections/declaration/d-base.html', context)
        





@login_required(login_url='login')
def application_saved(request, pk):
    
    try:
        application = get_object_or_404(Application, id=pk)
    except Http404:
        return render(request, 'admission/errors/application_404.html')
    
    if not application.owner == request.user:
        return render(request, 'admission/errors/application_403.html')
    
    if application.application_status == ApplicationStatus.PENDING_DEPOSIT_VERIFICATION:
        return redirect('dashboard')
    
    if request.user.is_authenticated:
        logout(request)
    
    course_code = application.selected_course.code
    course_details = Course.objects.values('code', 'title', 'campus').get(code=course_code)
    
    context = {
        'application': application,
        'course_details': course_details
    }
    
    return render(request, 'admission/application/application-saved.html', context)

import os



from admission.utils.generate_admission_pdf import generate_admission_pdf
from admission.utils.get_documents import get_secondary_documents, get_tertiary_documents
@login_required(login_url='login')
def download_application(request, pk):
    
    # create a zip buffer
    zip_buffer = BytesIO()
    
    # get application
    application = Application.objects.get(id=pk)
    
    # get tertiary_documents
    tertiary_documents = get_tertiary_documents(application)
    
    # get secondary_documents
    secondary_documents = get_secondary_documents(application)
    
    # generate admission pdf file
    pdf = generate_admission_pdf(application)
    pdf_filename = "Admission_Form__%s.pdf" % (f'{application.last_name.upper()}_{application.first_name.upper()}')
        
    # open zip buffer
    with zipfile.ZipFile(zip_buffer, 'w') as zipf:
        
        # write pdf to zip buffer
        zipf.writestr(pdf_filename, pdf.getvalue())

        # get documents associated with application (e.g. receipt, slip, medical_report)
        # write them to zip buffer
        
        # medical_report
        try:
            filename, content = fetch_document_from_cloud(application, 'medical_report')
            zipf.writestr(filename, content.getvalue())
        except:
            pass
        
        # sponsorship_letter
        try:
            filename, content = fetch_document_from_cloud(application, 'sponsorship_letter')
            zipf.writestr(filename, content.getvalue())
        except:
            pass
        
        # deposit slip
        try:
            filename, content = fetch_document_from_cloud(application, 'deposit_slip')
            zipf.writestr(filename, content.getvalue())
        except:
            pass
        
        # receipt
        try:
            filename, content = fetch_document_from_cloud(application, 'receipt')
            zipf.writestr(filename, content.getvalue())
        except:
            pass
 
        
        # get all tertiary documents
        for document in tertiary_documents:      
            try:
                filename, content = fetch_single_doc_from_cloud(document)
                zipf.writestr(filename, content.getvalue())
            except:
                pass
            
        # get all tertiary documents
        for document in secondary_documents:         
            try:
                filename, content = fetch_single_doc_from_cloud(document)
                zipf.writestr(filename, content.getvalue())
            except:
                pass
            
    response = StreamingHttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    
    zip_filename = f"Admission_Application__{application.last_name.upper()}_{application.first_name.upper()}.zip"
    content = f"attachment; filename={zip_filename}"
    response['Content-Disposition'] = content
    
    return response



def fetch_single_doc_from_cloud(document):
    
    b2_api = B2Api()
    b2_api.authorize_account(
        "production", 
        settings.AWS_ACCESS_KEY_ID, 
        settings.AWS_SECRET_ACCESS_KEY
    )
    
    instance_filename = document.file.name
        
    file_info = b2_api.get_file_info_by_name(settings.AWS_STORAGE_BUCKET_NAME, instance_filename)
    
    file_content = BytesIO()
    b2_api.download_file_by_id(file_info.id_).save(file_content)

    return instance_filename, file_content

def fetch_document_from_cloud(instance, attribute):
    
    b2_api = B2Api()
    b2_api.authorize_account(
        "production", 
        settings.AWS_ACCESS_KEY_ID, 
        settings.AWS_SECRET_ACCESS_KEY
    )
    
    instance_url = getattr(instance, attribute).url
    instance_filename = getattr(instance, attribute).name

    parsed_url = urlparse(instance_url)
    path_components = parsed_url.path.split('/')
    
    file_name = '/'.join(path_components[2:]) # this is the same as instance_filename
    
    file_info = b2_api.get_file_info_by_name(settings.AWS_STORAGE_BUCKET_NAME, file_name)
    
    file_content = BytesIO()
    b2_api.download_file_by_id(file_info.id_).save(file_content)
    
    return instance_filename, file_content
    
    
    