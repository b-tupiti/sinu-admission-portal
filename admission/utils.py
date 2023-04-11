from .models import Application

def get_totals():
    
    total = Application.objects.all().count()
    pending = Application.objects.filter(application_state=Application.ApplicationState.PENDING).count()
    under_assessment = Application.objects.filter(application_state=Application.ApplicationState.UNDER_ASSESSMENT).count()
    offer_letter_issued = Application.objects.filter(application_state=Application.ApplicationState.OFFER_LETTER_ISSUED).count()
    cleared_for_enrolment = Application.objects.filter(application_state=Application.ApplicationState.CLEARED_FOR_ENROLLMENT).count()
    enrolment_complete = Application.objects.filter(application_state=Application.ApplicationState.ENROLLMENT_COMPLETE).count()
    
    totals = {
        'total': total,
        'in_process': total - enrolment_complete,
        'pending':pending,
        'under_assessment': under_assessment,
        'offer_letter_issued': offer_letter_issued,
        'cleared_for_enrolment': cleared_for_enrolment,
        'enrolment_complete': enrolment_complete,
    }
    
    return totals