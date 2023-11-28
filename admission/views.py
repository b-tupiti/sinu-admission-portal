from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models.application import Application, ApplicationStatus, Section
from .models.tertiary_qualification import TertiaryQualification
from .models.document import TQDocument
from .models.employment import Employment
from courses.models.course import Course
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login
from users.utils import create_applicant_account
from django.http import Http404, HttpResponse
from .utils.new_application import create_new_admission_application_for_user
from .utils.request_helpers import (
    is_put_request, 
    param_not_found_or_empty
)
from .utils.application_updates import (
    save_current_section, # should be updating furthest section here
    change_current_section, 
    get_tertiary_qualifications, 
    get_hs_qualifications,
    handle_submission,
)
from courses.utils import course_does_not_exist
import io
from django.http import FileResponse
from admission.utils.generators import render_to_pdf
import zipfile
from io import BytesIO
from django.core.files.base import ContentFile
from django.db.utils import IntegrityError

    
def create_new_application(request):
    """
    This view expects a course_code parameter on a GET request, which will be used
    when a subsequent POST request is made to create a new admission application. 
    
    If this parameter is not present, has an empty value, or the value does not match a Course instance, the user
    will be redirected to the 'search-course' url. The assumption is that we are creating a new application
    for a course, hence it must have existed beforehand.
    """
    
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
                application.save()
                return redirect('application-saved', pk=application.id)
            
            elif 'submit_application' in request.POST:
                handle_submission(request, application)
                # application.application_status = ApplicationStatus.PENDING_DEPOSIT_VERIFICATION
                # application.is_declared = True
                # application.save()
                return redirect('dashboard')

            else:   
                application = save_current_section(request, application)
        
        application.save()
    
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
    
    context = {
        'application': application,
    }
    
    return render(request, 'admission/application/application-saved.html', context)

import os

@login_required(login_url='login')
def download_application(request, pk):
    
    # get all documents associated with application
    
    application = Application.objects.get(id=pk)
    documents = get_documents(application)
    t_qualifications = get_tertiary_qualifications(application)
    context = {
        'application': application,
        't_qualifications': t_qualifications
    }
    context['current_employment'] = Employment.objects.filter(is_current=True, application=application).first()
    context['previous_employments'] = Employment.objects.filter(is_current=False, application=application)
    
    pdf = render_to_pdf('admission/pdf_templates/admission_form.html', context)
    zip_buffer = BytesIO()
    
    # Create a ZIP file and add the PDF to it
    with zipfile.ZipFile(zip_buffer, 'w') as zipf:
        
        # You can set the PDF filename within the ZIP file here
        pdf_filename = "Admission_Form__%s.pdf" % (f'{application.last_name.upper()}_{application.first_name.upper()}')
        zipf.writestr(pdf_filename, pdf.getvalue())
        
        for document in documents:
            with open(document.file.path, 'rb') as file:
                file_content = file.read()
                doc_filename = f"docs/{os.path.basename(document.file.name)}"
                zipf.writestr(doc_filename, file_content)
        
        # Add the receipt file 
        if application.receipt:
            with open(application.receipt.path, 'rb') as receipt_file:
                receipt_content = receipt_file.read()
                receipt_filename = os.path.basename(application.receipt.name)
                zipf.writestr(receipt_filename, receipt_content)  
                
        # Add the deposit slip / tt 
        if application.deposit_slip:
            with open(application.deposit_slip.path, 'rb') as deposit_file:
                deposit_content = deposit_file.read()
                deposit_filename = os.path.basename(application.deposit_slip.name)
                zipf.writestr(deposit_filename, deposit_content)
                
        # Add medical report 
        if application.medical_report:
            with open(application.medical_report.path, 'rb') as file:
                content = file.read()
                filename = os.path.basename(application.medical_report.name)
                zipf.writestr(filename, content)    
        
        # Add high school documents        
        hs_documents = application.high_school_documents.all()
        for document in hs_documents:
            with open(document.file.path, 'rb') as deposit_file:
                document_content = document.file.read()
                document_filename = f"docs/{os.path.basename(document.file.name)}"
                zipf.writestr(document_filename, document_content) 

    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    
    zip_filename = f"Admission_Application__{application.last_name.upper()}_{application.first_name.upper()}.zip"
    content = f"attachment; filename={zip_filename}"
    response['Content-Disposition'] = content
    
    return response

def get_documents(application):
    
    # Tertiary Docs
    tertiary_qualifications = TertiaryQualification.objects.filter(application=application)
    documents = []
    for qualification in tertiary_qualifications:
        documents.extend(TQDocument.objects.filter(qualification=qualification))
        
    return documents
    
