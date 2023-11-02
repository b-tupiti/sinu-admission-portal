from admission.models.application import Application, ApplicationStatus
from utils.send_mail import send_mail

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
            

def send_application_created_email(instance):
    
    # send new application created email
    subject = "Application {instance.id} created"
    message = "You started a new application."
    send_mail(instance.applicant.email, subject, message)