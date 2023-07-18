from .models import ApplicationState, Application, Section
from courses.models.course import Course
from utils.convert_date import convert_date_format
from django.shortcuts import redirect


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
    application.sponsor_type = _sponsor_type(request.POST.get('sponsor_type'))
    application.sponsor_name = request.POST.get('sponsor_name')
    application.sponsor_email = request.POST.get('sponsor_email')
    application.sponsor_phone_number = request.POST.get('sponsor_phone_number')
    application.sponsor_address = request.POST.get('sponsor_address')
    application.save()
    
def _sponsor_type(sponsor_type):
    if sponsor_type == 'Private':
        return 'private'
    elif sponsor_type == 'Private with concession (staff)':
        return 'private_with_concession'
    elif sponsor_type == 'Sponsored':
        return 'sponsored'










def get_totals():
    
    total = Application.objects.all().count()
    pending = Application.objects.filter(application_state=ApplicationState.SUBMITTED).count()
    under_assessment = Application.objects.filter(application_state=ApplicationState.DRAFT).count()

    
    totals = {
        'total': total,
        # 'in_process': total - enrolment_complete,
        # 'pending':pending,
        # 'under_assessment': under_assessment,
        # 'offer_letter_issued': offer_letter_issued,
        # 'cleared_for_enrolment': cleared_for_enrolment,
        # 'enrolment_complete': enrolment_complete,
    }
    
    return totals


def section_icon_clicked(request):
    return request.POST.get('_method') == 'put'


from enum import Enum

class ESection(Enum):
    PERSONAL_DETAILS = 'personal_details'
    SPONSOR_DETAILS = 'sponsor_details'
    EDUCATION_BACKGROUND = 'education_background'
    EMPLOYMENT_HISTORY = 'employment_history'
    DECLARATION = 'declaration'


def update_current_section(request, application):
    
   
            
    if ESection.PERSONAL_DETAILS.value in request.POST:
        
        if application.current_section not in [
            Section.EDUCATION_BACKGROUND, 
            Section.EMPLOYMENT_HISTORY, 
            Section.DECLARATION]:
                application.current_section = Section.SPONSOR_DETAILS
            
        application.edit_section = Section.SPONSOR_DETAILS
        
    elif ESection.SPONSOR_DETAILS.value in request.POST:
        
        if application.current_section not in [
            Section.EMPLOYMENT_HISTORY, 
            Section.DECLARATION]:
                application.current_section = Section.EDUCATION_BACKGROUND
                
        application.edit_section = Section.EDUCATION_BACKGROUND
        
    elif ESection.EDUCATION_BACKGROUND.value in request.POST:
        
        if application.current_section not in [
            Section.DECLARATION]:
                application.current_section = Section.EMPLOYMENT_HISTORY
        
        application.edit_section = Section.EMPLOYMENT_HISTORY
        
    elif ESection.EMPLOYMENT_HISTORY.value in request.POST:
        application.current_section = Section.DECLARATION
        application.edit_section = Section.DECLARATION
        
    else:      
        application.current_section = Section.PERSONAL_DETAILS
        application.edit_section = Section.PERSONAL_DETAILS
    
    
        
    return application




def change_edit_section(request, application):
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