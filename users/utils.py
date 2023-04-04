from mbasubmission.models import Application
from django.db.models import Q
from django.contrib.auth.models import Group

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