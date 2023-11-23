from admission.models.application import Application, ApplicationStatus
from utils.send_mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import settings


def send_email_based_on_application_status(instance):
    
    original_instance = Application.objects.get(id=instance.id)
    
    
    if original_instance.application_status != instance.application_status:
        
        
        
        if instance.application_status == ApplicationStatus.PENDING_DEPOSIT_VERIFICATION:
            
            # send mail to user email, application has been received.
            subject = "Application Received"
            message = f"Hi {instance.first_name},\n\n Your Application has been Recieved."
            send_mail(instance.applicant.email, subject, message)
            
            # send mail to finance.admissions@sinu.edu.sb, application ready for verification.
            subject = "Application ID {instance.id} is ready for deposit Verification."
            message = "Att: Finance,\n\n Application ID {instance.id} is ready for deposit verification.\n\n"
            send_mail('finance.admissions@sinu.edu.sb', subject, message)
            
        elif instance.application_status == ApplicationStatus.UNDER_ASSESSMENT:
                    
            # send mail to sas.admissions@sinu.edu.sb, application is verified from finance.
            subject = "Application {instance.id} has been cleared for Assessment"
            message = f"Att: SAS,\n\n Application ID {instance.id} is ready for Assessment.\n\n"
            send_mail('sas.admissions@sinu.edu.sb', subject, message)
        
        elif instance.application_status == ApplicationStatus.APPROVED_AND_OFFER_GRANTED:
            
            # send mail to user email, offer letter granted, attach offer letter.
            subject = "Application {instance.id} Outcome"
            message = f"Hi {instance.first_name},\n\n Congratulations.\n\nPlease find your letter of offer attached."
            send_mail(instance.applicant.email, subject, message)
            
            # send mail to sas.admissions@sinu.edu.sb, application is verified from finance.
            subject = "Application {instance.id} granted Offer"
            message = f"Att: SAS,\n\n Application ID {instance.id} has been granted a letter of offer.\n\n"
            send_mail('sas.admissions@sinu.edu.sb', subject, message)
            

from django.template.loader import render_to_string
def send_application_created_email(instance):
    
    applicant_username = f'{instance.applicant}'
    applicant_name = f'{instance.first_name} {instance.last_name}'.title()
    course_title = f'{instance.selected_course.title.title()}'
    
    subject = f"Your application for {course_title}"
    
    context = {
        'applicant_username': applicant_username,
        'applicant_name': applicant_name,
        'course_title': course_title,
    }
    html_content = render_to_string('admission/email_templates/thank-you-for-starting-new-application.html', context)
    from_email = 'study@sinu.edu.sb'
    
    mail_obj = Mail(
        from_email=from_email,
        to_emails=instance.applicant.email,
        subject=subject,
        html_content=html_content,
    )
    
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(mail_obj)
        print(response.status_code)
        
    except Exception as e:
        print(str(e))