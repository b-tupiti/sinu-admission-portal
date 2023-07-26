from django.db import IntegrityError
from .models.application import ApplicationState, Application, Section
from .models.document import SponsorshipLetter, HSDocument, HSFormLevel, DocumentType
from courses.models.course import Course
from utils.convert_date import convert_date_format
from enum import Enum


class ESection(Enum):
    PERSONAL_DETAILS = 'personal_details'
    SPONSOR_DETAILS = 'sponsor_details'
    EDUCATION_BACKGROUND = 'education_background'
    EMPLOYMENT_HISTORY = 'employment_history'
    DECLARATION = 'declaration'


def get_course_from_code(request):
    course_code = request.GET.get('course_code')
    course =  Course.objects.values('code', 'title', 'campus').get(code=course_code)
    return course


def create_new_admission_application_for_user(user, course):
    application = Application.objects.create(
                applicant=user,
                selected_course=course,
                first_name=user.first_name,
                middle_name=user.middle_name,
                last_name=user.last_name,
                date_of_birth=user.date_of_birth,
                gender=user.gender,
            )
    return application


def save_personal_details(request, application):
    application.first_name = request.POST.get('first_name')
    application.middle_name = request.POST.get('middle_name')
    application.last_name = request.POST.get('last_name')
    application.gender = request.POST.get('gender')
    application.date_of_birth = convert_date_format(request.POST.get('date_of_birth'))
    application.save()
    
    
def save_sponsor_details(request, application):
    
    if request.FILES.get('sponsorship_letter'):          
       _save_or_replace_sponsorship_letter(request, application)
            
    application.sponsor_type = _sponsor_type(request.POST.get('sponsor_type'))
    application.sponsor_name = request.POST.get('sponsor_name')
    application.sponsor_email = request.POST.get('sponsor_email')
    application.sponsor_phone_number = request.POST.get('sponsor_phone_number')
    application.sponsor_address = request.POST.get('sponsor_address')
    application.save()

  
def _save_or_replace_sponsorship_letter(request, application):
    try:
            
            letter = SponsorshipLetter(
                file=request.FILES.get('sponsorship_letter'),
                application=application,
            )
            letter.save()
            
    except IntegrityError as e:
        
        SponsorshipLetter.objects.filter(application=application).delete()
        letter = SponsorshipLetter(
            file=request.FILES.get('sponsorship_letter'),
            application=application,
        )
        
        letter.save() 
        
    
def _sponsor_type(sponsor_type):
    if sponsor_type == 'Private':
        return 'private'
    elif sponsor_type == 'Private with concession (staff)':
        return 'private_with_concession'
    elif sponsor_type == 'Sponsored':
        return 'sponsored'


def _save_or_replace_document(file, application, document_type, form_level):
        
    document = HSDocument.objects.filter(
            application=application,
            form_level=form_level, 
            document_type=document_type
            )
    
    if document.exists():
        document.delete()
        print('document exists already, deleting it, ready for replacement.')
    
    document = HSDocument(
        file=file,
        application=application,
        form_level=form_level, 
        document_type=document_type
    )
    
    document.save()
            
    
    
def save_education_background(request, application):
    
    # form 3 documents
    if request.FILES.get('form_3_certificate'):
       file = request.FILES.get('form_3_certificate')          
       _save_or_replace_document(file, application, DocumentType.CERTIFICATE, HSFormLevel.FORM_3)
       
    if request.FILES.get('form_3_transcript'):
       file = request.FILES.get('form_3_transcript')          
       _save_or_replace_document(file, application, DocumentType.TRANSCRIPT, HSFormLevel.FORM_3)
    
    # form 5 documents  
    if request.FILES.get('form_5_certificate'):
       file = request.FILES.get('form_5_certificate')          
       _save_or_replace_document(file, application, DocumentType.CERTIFICATE, HSFormLevel.FORM_5)
       
    if request.FILES.get('form_5_transcript'):
       file = request.FILES.get('form_5_transcript')          
       _save_or_replace_document(file, application, DocumentType.TRANSCRIPT, HSFormLevel.FORM_5)
       
    # form 6 documents  
    if request.FILES.get('form_6_certificate'):
       file = request.FILES.get('form_6_certificate')          
       _save_or_replace_document(file, application, DocumentType.CERTIFICATE, HSFormLevel.FORM_6)
       
    if request.FILES.get('form_6_transcript'):
       file = request.FILES.get('form_6_transcript')          
       _save_or_replace_document(file, application, DocumentType.TRANSCRIPT, HSFormLevel.FORM_6)
       
    # foundation documents  
    if request.FILES.get('foundation_certificate'):
       file = request.FILES.get('foundation_certificate')          
       _save_or_replace_document(file, application, DocumentType.CERTIFICATE, HSFormLevel.FOUNDATION)
       
    if request.FILES.get('foundation_transcript'):
       file = request.FILES.get('foundation_transcript')          
       _save_or_replace_document(file, application, DocumentType.TRANSCRIPT, HSFormLevel.FOUNDATION)
       
    application.third_form_school = request.POST.get('third_form_school')
    application.third_form_year = request.POST.get('third_form_year')
    application.fifth_form_school = request.POST.get('fifth_form_school')
    application.fifth_form_year = request.POST.get('fifth_form_year')
    application.sixth_form_school = request.POST.get('sixth_form_school')
    application.sixth_form_year = request.POST.get('sixth_form_year')
    application.foundation_school = request.POST.get('foundation_school')
    application.foundation_year = request.POST.get('foundation_year')
    application.save()


def is_put_request(request):
    """
    checks if the request object actually simulates a PUT request.
    """
    return request.method == 'POST' and request.POST.get('_method') == 'put'
     


# This function fires when the next button is clicked, it checks where the current section is
# and sets the new current section to the one on its right. It always goes left --> right
def update_current_section(request, application):
       
    if ESection.PERSONAL_DETAILS.value in request.POST:
        
        if application.current_section not in [
            Section.EDUCATION_BACKGROUND, 
            Section.EMPLOYMENT_HISTORY, 
            Section.DECLARATION]:
                save_personal_details(request, application)
                application.current_section = Section.SPONSOR_DETAILS
            
        application.edit_section = Section.SPONSOR_DETAILS
        
    elif ESection.SPONSOR_DETAILS.value in request.POST:
        
        if application.current_section not in [
            Section.EMPLOYMENT_HISTORY, 
            Section.DECLARATION]:
                save_sponsor_details(request, application)
                application.current_section = Section.EDUCATION_BACKGROUND
                
        application.edit_section = Section.EDUCATION_BACKGROUND
        
    elif ESection.EDUCATION_BACKGROUND.value in request.POST:
        
        if application.current_section not in [
            Section.DECLARATION]:
                save_education_background(request, application)
                application.current_section = Section.EMPLOYMENT_HISTORY
        
        application.edit_section = Section.EMPLOYMENT_HISTORY
        
    elif ESection.EMPLOYMENT_HISTORY.value in request.POST:
        application.current_section = Section.DECLARATION
        application.edit_section = Section.DECLARATION
        
    else:      
        application.current_section = Section.PERSONAL_DETAILS
        application.edit_section = Section.PERSONAL_DETAILS
       
    return application


def update_edit_section(request, application):
    if ESection.PERSONAL_DETAILS.value in request.POST:    
        application.edit_section = Section.PERSONAL_DETAILS
                     
    elif ESection.SPONSOR_DETAILS.value in request.POST:
        application.edit_section = Section.SPONSOR_DETAILS
    
    elif ESection.EDUCATION_BACKGROUND.value in request.POST:
        application.edit_section = Section.EDUCATION_BACKGROUND
        
    elif ESection.EMPLOYMENT_HISTORY.value in request.POST:
        application.edit_section = Section.EMPLOYMENT_HISTORY
    
    elif ESection.DECLARATION.value in request.POST:
        application.edit_section = Section.DECLARATION
            
    return application


def add_documents_to_context(documents, application, context):
    form_3_certificate = documents.filter(
        application=application,
        form_level=HSFormLevel.FORM_3,
        document_type=DocumentType.CERTIFICATE
        ).first()
    context['form_3_certificate'] = form_3_certificate
        
    form_3_transcript = documents.filter(
        application=application,
        form_level=HSFormLevel.FORM_3,
        document_type=DocumentType.TRANSCRIPT
        ).first()
    context['form_3_transcript'] = form_3_transcript
        
    form_5_certificate = documents.filter(
        application=application,
        form_level=HSFormLevel.FORM_5,
        document_type=DocumentType.CERTIFICATE
        ).first()
    context['form_5_certificate'] = form_5_certificate
    
    form_5_transcript = documents.filter(
        application=application,
        form_level=HSFormLevel.FORM_5,
        document_type=DocumentType.TRANSCRIPT
        ).first()
    context['form_5_transcript'] = form_5_transcript
        
    form_6_certificate = documents.filter(
        application=application,
        form_level=HSFormLevel.FORM_6,
        document_type=DocumentType.CERTIFICATE
        ).first()
    context['form_6_certificate'] = form_6_certificate
    
    form_6_transcript = documents.filter(
        application=application,
        form_level=HSFormLevel.FORM_6,
        document_type=DocumentType.TRANSCRIPT
        ).first()
    context['form_6_transcript'] = form_6_transcript
    
    foundation_certificate = documents.filter(
        application=application,
        form_level=HSFormLevel.FOUNDATION,
        document_type=DocumentType.CERTIFICATE
        ).first()
    context['foundation_certificate'] = foundation_certificate
    
    foundation_transcript = documents.filter(
        application=application,
        form_level=HSFormLevel.FOUNDATION,
        document_type=DocumentType.TRANSCRIPT
        ).first()
    context['foundation_transcript'] = foundation_transcript
    
    return context