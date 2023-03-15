from django.db.models.signals import post_save
from mbasubmission.models import Application
from django.core.mail import send_mail
from config import settings
from django.dispatch import receiver
import time
import threading
from django.template.loader import render_to_string

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


        
