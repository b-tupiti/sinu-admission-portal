from .models import ApplicationState, Application


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