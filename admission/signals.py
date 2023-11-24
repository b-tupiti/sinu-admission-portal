from django.dispatch import receiver
from admission.utils.application_perms import (
    set_permissions_based_on_application_status,
)
from admission.utils.admission_emails import (
    send_email_based_on_application_status,
    send_application_created_email
)
from .models.application import Application
from django.db.models.signals import (
    pre_save,
    post_save,
)

@receiver(pre_save, sender=Application)
def before_instance_is_saved(sender, instance, **kwargs):
    
    if not instance._state.adding:
        set_permissions_based_on_application_status(instance)
        
    else:
        send_application_created_email(instance)
        
@receiver(post_save, sender=Application)
def after_instance_is_saved(sender, instance, **kwargs):
    send_email_based_on_application_status(instance)