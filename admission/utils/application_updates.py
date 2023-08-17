from enum import Enum
import json
from django.db import IntegrityError
from admission.models.application import Section
from admission.models.document import DocumentType, HSDocument, HSFormLevel, SponsorshipLetter
from utils.convert_date import convert_date_format
from .request_helpers import param_not_found_or_empty
from admission.models.tertiary_qualification import TertiaryQualification


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


class ESection(Enum):
    PERSONAL_DETAILS = 'personal_details'
    SPONSOR_DETAILS = 'sponsor_details'
    EDUCATION_BACKGROUND = 'education_background'
    EMPLOYMENT_HISTORY = 'employment_history'
    DECLARATION = 'declaration'

# This function fires when the next button is clicked, it checks where the current section is
# and sets the new current section to the one on its right. It always goes left --> right
def update_current_section(request, application):
    """
    This function handles POST data when a section is saved.
    """
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


def save_education_background(request, application):
    
    # deletes the tertiary qualifications selected by the user, if there is any.
    if not param_not_found_or_empty(request.POST.get('delete-ids')):
        deleteIds = json.loads(request.POST.get('delete-ids'))
        for id in deleteIds:
            TertiaryQualification.objects.get(id=id).delete()
            
    
    # adding new qualification instances
    fields_list = [(str(key), request.POST[key]) for key in request.POST.keys() if key.startswith('new')]
    unique_ids = []
    grouped_fields = dict()

    for field_item in fields_list:
        id = field_item[0].split('-')[-1] 
        
        if id not in unique_ids:
            unique_ids.append(id)
            grouped_fields[id] = []
            grouped_fields[id].append(field_item)
            
        else:
            grouped_fields[id].append(field_item)

    for group in list(grouped_fields.values()):
        qualification = dict()
        
        for field_item in group:
            key = str(field_item[0]).split('-')[-2]
            qualification[key] = field_item[1]
        
        TertiaryQualification.objects.create(
            application=application,
            institution_name=qualification['institution'],
            course=qualification['course'],
            year_start=qualification['year_started'],
            year_end=qualification['year_ended'],
            major=qualification['major'],
        )
    
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
