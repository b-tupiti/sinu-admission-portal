from enum import Enum
from django.forms import model_to_dict
from admission.models.application import Section
from admission.models.document import DocumentType, HSFormLevel
from admission.utils.section_save_update.education_background import save_education_background
from admission.utils.section_save_update.employment_history import save_employment_history
from utils.convert_date import convert_date_format
from django.utils import timezone

def handle_submission(request, application):
    from admission.models.application import ApplicationStatus
    try:
        application.deposit_slip = request.FILES.get('deposit_slip')
    except:
        pass
    application.application_status = ApplicationStatus.PENDING_DEPOSIT_VERIFICATION
    application.is_declared = True
    application.date_submitted = timezone.now()
    application.save()
    

def _sponsor_type(sponsor_type):
    if sponsor_type == 'Private':
        return 'private'
    elif sponsor_type == 'Private with concession (staff)':
        return 'private_with_concession'
    elif sponsor_type == 'Sponsored':
        return 'sponsored'


class ESection(Enum):
    PERSONAL_DETAILS = 'personal_details'
    SPONSOR_DETAILS = 'sponsor_details'
    EDUCATION_BACKGROUND = 'education_background'
    EMPLOYMENT_HISTORY = 'employment_history'
    DECLARATION = 'declaration'


## This function needs a review: It should not have any side effects
def save_current_section(request, application):
    """
    saves current section, sets new current section.
    """
    try:
        current_section = request.POST.get('current_section')
        
        if (current_section == Section.PERSONAL_DETAILS):
            save_personal_details(request, application)
            application.current_section = Section.SPONSOR_DETAILS
        
        elif (current_section == Section.SPONSOR_DETAILS):
            save_sponsor_details(request, application)
            application.current_section = Section.EDUCATION_BACKGROUND
        
        elif (current_section == Section.EDUCATION_BACKGROUND):
            save_education_background(request, application)
            application.current_section = Section.EMPLOYMENT_HISTORY
        
        elif (current_section == Section.EMPLOYMENT_HISTORY):
            save_employment_history(request, application)
            application.current_section = Section.DECLARATION
    finally:
        return application
        

def save_current_section_modified(request, application):
    try:
        current_section = request.POST.get('current_section')
        
        if (current_section == Section.PERSONAL_DETAILS):
            save_personal_details(request, application)
        
        elif (current_section == Section.SPONSOR_DETAILS):
            save_sponsor_details(request, application)
        
        elif (current_section == Section.EDUCATION_BACKGROUND):
            save_education_background(request, application)
        
        elif (current_section == Section.EMPLOYMENT_HISTORY):
            save_employment_history(request, application)
    finally:
        application.save()
        return application

def save_personal_details(request, application):
    
    if request.FILES.get('medical_report'):    
        application.medical_report = request.FILES.get('medical_report')

    # temporarily handling dropdown fields: gender, title marital_status
    if request.POST.get('title') != 'Please select':
        application.title = request.POST.get('title')
    if request.POST.get('gender') != 'Please select':
        application.gender = request.POST.get('gender')
    if request.POST.get('marital_status') != 'Please select':
        application.marital_status = request.POST.get('marital_status')
    if request.POST.get('province') != 'Please select':
        application.province = request.POST.get('province')
    if request.POST.get('constituency') != 'Please select':
        application.constituency = request.POST.get('constituency')
    if request.POST.get('country_of_birth') != 'Please select':
        application.country_of_birth = request.POST.get('country_of_birth')
    if request.POST.get('citizenship') != 'Please select':
        application.citizenship = request.POST.get('citizenship')
        
    application.student_id = request.POST.get('student_id')
    application.first_name = request.POST.get('first_name')
    application.middle_name = request.POST.get('middle_name')
    application.last_name = request.POST.get('last_name')
    
    application.date_of_birth = convert_date_format(request.POST.get('date_of_birth'))
    
    application.mobile_phone_number = request.POST.get('mobile_phone_number')
    application.telephone_number = request.POST.get('telephone_number')
    application.permanent_address = request.POST.get('permanent_address')
    application.contact_postal = request.POST.get('contact_postal')
    
    application.guardian_name = request.POST.get('guardian_name')
    application.guardian_address = request.POST.get('guardian_address')
    application.guardian_phone_number = request.POST.get('guardian_phone_number')
    application.ward = request.POST.get('ward')
    
    application.save()
    
    
def save_sponsor_details(request, application):
    
    if request.FILES.get('sponsorship_letter'):    
        application.sponsorship_letter = request.FILES.get('sponsorship_letter')
       
    application.sponsor_type = _sponsor_type(request.POST.get('sponsor_type'))
    application.sponsor_name = request.POST.get('sponsor_name')
    application.sponsor_email = request.POST.get('sponsor_email')
    application.sponsor_phone_number = request.POST.get('sponsor_phone_number')
    application.sponsor_address = request.POST.get('sponsor_address')
    application.save()



def change_current_section(request, application):
    if ESection.PERSONAL_DETAILS.value in request.POST:    
        application.current_section = Section.PERSONAL_DETAILS
                     
    elif ESection.SPONSOR_DETAILS.value in request.POST:
        application.current_section = Section.SPONSOR_DETAILS
    
    elif ESection.EDUCATION_BACKGROUND.value in request.POST:
        application.current_section = Section.EDUCATION_BACKGROUND
        
    elif ESection.EMPLOYMENT_HISTORY.value in request.POST:
        application.current_section = Section.EMPLOYMENT_HISTORY
    
    elif ESection.DECLARATION.value in request.POST:
        application.current_section = Section.DECLARATION
            
    return application


def filter_document(documents, form_level, doc_type):
    
    document = documents.filter(form_level=form_level, document_type=doc_type).first()
    return document


    
def get_hs_qualifications(application):
    
    documents = application.high_school_documents.all()
    
    hs_qualifications = [
        generate_dict(HSFormLevel.FORM_3, application, documents),
        generate_dict(HSFormLevel.FORM_5, application, documents),
        generate_dict(HSFormLevel.FORM_6, application, documents),
        generate_dict(HSFormLevel.FOUNDATION, application, documents),
    ]

    return hs_qualifications


def generate_dict(level, application, documents):
    
    school_dict = dict()
    
    if level == HSFormLevel.FORM_6:
        
        school_dict['school'] = application.sixth_form_school
        school_dict['year'] = application.sixth_form_year
        school_dict['file_input_name_prefix'] = 'form_6_'
        school_dict['input_name_prefix'] = 'sixth_form_'
        school_dict['level_description'] = 'Sixth Form'
        
    elif level == HSFormLevel.FORM_3:
        
        school_dict['school'] = application.third_form_school
        school_dict['year'] = application.third_form_year
        school_dict['file_input_name_prefix'] = 'form_3_'
        school_dict['input_name_prefix'] = 'third_form_'
        school_dict['level_description'] = 'Third Form'
        
    elif level == HSFormLevel.FORM_5:
        
        school_dict['school'] = application.fifth_form_school
        school_dict['year'] = application.fifth_form_year
        school_dict['file_input_name_prefix'] = 'form_5_'
        school_dict['input_name_prefix'] = 'fifth_form_'
        school_dict['level_description'] = 'Fifth Form'
        
    elif level == HSFormLevel.FOUNDATION:
        
        school_dict['school'] = application.foundation_school
        school_dict['year'] = application.foundation_year
        school_dict['file_input_name_prefix'] = 'foundation_'
        school_dict['input_name_prefix'] = 'foundation_'
        school_dict['level_description'] = 'Foundation'
        
    
    school_dict['documents'] = {
                'certificate': {
                    'name': filter_document(documents, level, DocumentType.CERTIFICATE)
                },
                'transcript': {
                    'name': filter_document(documents, level, DocumentType.TRANSCRIPT)
                }
            }
    
    return school_dict


def get_tertiary_qualifications(application):
    
    # grab all tertiary qualifications
    tq_qset = application.tertiary_qualifications.all()
    
    # create empty list for tertiary qualifications
    tertiary_qualifications = []

    # loop through tertiary qualifications queryset
    for q_obj in tq_qset:
        
        # 1.
        # get dict object from tertiary qualification model
        obj_dict = model_to_dict(q_obj)
        
        # remove application item in dict object of qualification, for a leaner object
        obj_dict.pop('application')
        
        # 2.
        # get queryset of all tertiary documents related to qualification instance
        q_docs_set = q_obj.related_documents.all()
        
        certificate = q_docs_set.filter(document_type=DocumentType.CERTIFICATE).first()
        transcript = q_docs_set.filter(document_type=DocumentType.TRANSCRIPT).first()
        
        obj_dict['certificate'] = certificate
        obj_dict['transcript'] = transcript
        tertiary_qualifications.append(obj_dict)
        
        
    
    return tertiary_qualifications
        
    
    