from admission.models.application import Application
from django.db.models import Q
from django.contrib.auth.models import Group

from .models.user import User
from utils.convert_date import convert_date_format

def create_applicant_account(request):
    
    first_name = request.POST.get('first_name').lower()
    middle_name = request.POST.get('middle_name').lower()
    last_name = request.POST.get('last_name').lower()
    gender = request.POST.get('gender').lower()
    date_of_birth = convert_date_format(request.POST.get('date_of_birth'))
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    User.objects.create_user(
        email, 
        password, 
        first_name,
        middle_name,
        last_name,
        gender, 
        date_of_birth
    )
    
    return email, password


    
    













def filter_applications(request, filter):
    """
    filter for applications
    """
    applications = Application.objects.all()
    group = None
    
    
    if filter is None:
        
        try:
            if request.user.groups.filter(pk=Group.objects.get(name="Assesors").pk).exists():
                group = 'Assesors'
                applications = Application.objects.filter(
                    Q(application_state=Application.ApplicationState.UNDER_ASSESSMENT) 
                    )
            elif request.user.groups.filter(pk=Group.objects.get(name="Finance Department").pk).exists():
                group = 'Finance Department'
                applications = Application.objects.filter(
                    Q(application_state=Application.ApplicationState.OFFER_LETTER_ISSUED) 
                    )
            elif request.user.groups.filter(pk=Group.objects.get(name="Student Administration Services (SAS) Department").pk).exists():
                group = 'Student Administration Services (SAS) Department'
                applications = Application.objects.filter(
                    Q(application_state=Application.ApplicationState.PENDING) |  
                    Q(application_state=Application.ApplicationState.CLEARED_FOR_ENROLLMENT)
                    )
            else:
                applications = Application.objects.all()
        except:
            group = None
    else:
        group = get_group(request)
        if filter == 'all_verbose':
            applications = Application.objects.all()
           
        elif filter == 'pending':
            applications = Application.objects.filter(application_state=Application.ApplicationState.PENDING)
        elif filter == 'under_assesment':
            applications = Application.objects.filter(application_state=Application.ApplicationState.UNDER_ASSESSMENT)
        elif filter == 'offer_issued':
            applications = Application.objects.filter(application_state=Application.ApplicationState.OFFER_LETTER_ISSUED)
        elif filter == 'cleared_for_enrolment':
            applications = Application.objects.filter(application_state=Application.ApplicationState.CLEARED_FOR_ENROLLMENT)
        elif filter == 'enrolment_complete':
            applications = Application.objects.filter(application_state=Application.ApplicationState.ENROLLMENT_COMPLETE)
    
   
    
    return applications, group


def get_group(request):
    
    group = None
    
    try:
        if request.user.groups.filter(pk=Group.objects.get(name="Assesors").pk).exists():
            group = 'Assesors'
        elif request.user.groups.filter(pk=Group.objects.get(name="Finance Department").pk).exists():
            group = 'Finance Department'
        elif request.user.groups.filter(pk=Group.objects.get(name="Student Administration Services (SAS) Department").pk).exists():
            group = 'Student Administration Services (SAS) Department'
    except:
        group = None
    
    return group