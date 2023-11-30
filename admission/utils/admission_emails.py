from admission.models.application import Application, ApplicationStatus
from utils.send_mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, 
    Attachment, 
    FileContent, 
    FileName, 
    FileType, 
    Disposition
)
from config import settings
from django.template.loader import render_to_string


def send_email_based_on_application_status(instance):
    
    # original_instance = Application.objects.get(id=instance.id)
    
    
    # if original_instance.application_status != instance.application_status:
        
        
        
    if instance.application_status == ApplicationStatus.PENDING_DEPOSIT_VERIFICATION:
        
        # send mail to user email, application has been received.
        applicant_title = f'{instance.title}'
        applicant_username = f'{instance.applicant}'
        applicant_name = f'{instance.first_name} {instance.last_name}'.title()
        course_title = f'{instance.selected_course.title.title()}'
        
        subject = f"Your successfully submitted application for {course_title}"
        
        context = {
            'applicant_title': applicant_title,
            'applicant_username': applicant_username,
            'applicant_name': applicant_name,
            'course_title': course_title,
        }
        html_content = render_to_string('admission/email_templates/thank-you-for-submitting-your-application.html', context)
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
        
        # send mail to finance.admissions@sinu.edu.sb, application ready for verification.
        application_id = f'{instance.id}'
        applicant_username = f'{instance.applicant}'
        applicant_name = f'{instance.first_name} {instance.last_name}'.title()
        course_title = f'{instance.selected_course.title.title()}'
        
        subject = f"Application #{application_id} is awaiting Deposit Verification."
        
        context = {
            'application_id': application_id,
            'applicant_username': applicant_username,
            'applicant_name': applicant_name,
            'course_title': course_title,
        }
        html_content = render_to_string('admission/email_templates/application-is-awaiting-deposit-verification.html', context)
        from_email = 'noreply@sinu.edu.sb'
        to_email = 'finance.admissions@sinu.edu.sb'
        
        mail_obj = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content,
        )
        
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(mail_obj)
            print(response.status_code)
            
        except Exception as e:
            print(str(e))
        
    elif instance.application_status == ApplicationStatus.UNDER_ASSESSMENT:
                
        # send mail to applicant, application is moved forward for assessment.
        applicant_title = f'{instance.title}'
        applicant_username = f'{instance.applicant}'
        applicant_name = f'{instance.first_name} {instance.last_name}'.title()
        course_title = f'{instance.selected_course.title.title()}'
        
        subject = f"Your application for {course_title} is moved forward for assessment."
        
        context = {
            'applicant_title': applicant_title,
            'applicant_username': applicant_username,
            'applicant_name': applicant_name,
            'course_title': course_title,
        }
        html_content = render_to_string('admission/email_templates/your-deposit-slip-is-verified-and-application-is-under-assessment.html', context)
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
            
        # send mail to sas.admissions@sinu.edu.sb, application is verified from finance
        application_id = f'{instance.id}'
        applicant_username = f'{instance.applicant}'
        applicant_name = f'{instance.first_name} {instance.last_name}'.title()
        course_title = f'{instance.selected_course.title.title()}'
        
        subject = f"Application #{application_id} is ready for Assessment."
        
        context = {
            'application_id': application_id,
            'applicant_username': applicant_username,
            'applicant_name': applicant_name,
            'course_title': course_title,
        }
        html_content = render_to_string('admission/email_templates/application-is-ready-for-assessment.html', context)
        from_email = 'noreply@sinu.edu.sb'
        to_email = 'sas.admissions@sinu.edu.sb'
        
        mail_obj = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content,
        )
        
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(mail_obj)
            print(response.status_code)
            
        except Exception as e:
            print(str(e))
    
    elif instance.application_status == ApplicationStatus.APPROVED_AND_OFFER_GRANTED:
        
        # send mail to user email, offer letter granted, attach offer letter.
        applicant_title = f'{instance.title}'
        applicant_username = f'{instance.applicant}'
        applicant_name = f'{instance.first_name} {instance.last_name}'.title()
        course_title = f'{instance.selected_course.title.title()}'
        
        subject = f"Application Outcome."
        
        context = {
            'applicant_title': applicant_title,
            'applicant_username': applicant_username,
            'applicant_name': applicant_name,
            'course_title': course_title,
        }
        html_content = render_to_string('admission/email_templates/application-outcome.html', context)
        from_email = 'noreply@sinu.edu.sb'
        to_email = instance.applicant.email
        
        mail_obj = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content,
        )
        
        # Get the file from the model instance's file field
        # Retrieve environment variables from this env object
        import environ
        from config.settings import BASE_DIR
        env_file_path = BASE_DIR / '.env'
        env = environ.Env()
        env.read_env(env_file_path)
        
        if env('DJANGO_ENV') == 'production':
            attachment_file_path = instance.letter_of_offer.url
        else: 
            attachment_file_path = instance.letter_of_offer.path
            
        attachment_file_name = instance.letter_of_offer.name.split('/')[-1] 

        with open(attachment_file_path, 'rb') as file:
            file_data = file.read()

        import base64
        file_data_encoded = base64.b64encode(file_data).decode('utf-8')
        attachment = Attachment(
            FileContent(file_data_encoded),
            FileName(attachment_file_name),
            FileType('application/pdf'), 
            Disposition('attachment')
        )

        mail_obj.add_attachment(attachment)
        
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(mail_obj)
            print(response.status_code)
            
        except Exception as e:
            print(str(e))
        
        # send mail to sas.admissions@sinu.edu.sb.
        application_id = f'{instance.id}'
        applicant_username = f'{instance.applicant}'
        applicant_name = f'{instance.first_name} {instance.last_name}'.title()
        course_title = f'{instance.selected_course.title.title()}'
        
        subject = f"Application Outcome: Application #{application_id} has been granted admission."
        
        context = {
            'application_id': application_id,
            'applicant_username': applicant_username,
            'applicant_name': applicant_name,
            'course_title': course_title,
        }
        html_content = render_to_string('admission/email_templates/application-outcome-sas-confirmation.html', context)
        from_email = 'noreply@sinu.edu.sb'
        to_email = 'sas.admissions@sinu.edu.sb'
        
        mail_obj = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content,
        )
        
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(mail_obj)
            print(response.status_code)
            
        except Exception as e:
            print(str(e))
            


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