from django.db.models.signals import post_save
from mbasubmission.models import Application
from django.core.mail import send_mail
from config import settings
from django.dispatch import receiver
import time
import threading
from django.template.loader import render_to_string
import uuid
from django.urls import reverse

@receiver(post_save, sender=Application)
def send_confirmation_email(sender, instance, created, **kwargs):
    application = instance
    if created:
        subject = "Confirmation"
        message = "This is a confirmation email."
        context = {'application': application}
        html_message = render_to_string('mail/confirmation_email.html', context)
        def send_email():
            send_mail(
                subject, 
                message, 
                settings.EMAIL_HOST, 
                [application.email], 
                html_message=html_message,
                fail_silently=True,
            )
        threading.Thread(target=send_email).start()
    else:
        if application.application_state == Application.ApplicationState.OFFER_LETTER_ISSUED:
            
            token = str(uuid.uuid4())
            upload_url = f"{settings.BASE_URL}{reverse('upload_receipt')}?token={token}&id={application.id}"
        
            subject = "Congratulations! You have a provisional Offer Letter"
            context = {'application': application, 'upload_url':upload_url}
            html_message = render_to_string('mail/offer_issued_email.html', context)
            def send_email():
                send_mail(
                    subject, 
                    f'This email should include an Offer Letter, the proforma (invoice) for the MBA program, and SINU bank details so that the applicant can deposit.\nPlease click this link to upload your reciept: {upload_url}', 
                    settings.EMAIL_HOST, 
                    [application.email], 
                    html_message=html_message,
                    fail_silently=True,
                )
            threading.Thread(target=send_email).start()
            
           
        


        
