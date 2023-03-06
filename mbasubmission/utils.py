from .models import Application

def get_totals():
    
    total = Application.objects.all().count
    accepted = Application.objects.filter(application_state=Application.ApplicationState.ACCEPTED).count
    rejected = Application.objects.filter(application_state=Application.ApplicationState.REJECTED).count
    
    totals = {
        'total': total,
        'accepted':accepted,
        'rejected': rejected,
    }
    
    return totals