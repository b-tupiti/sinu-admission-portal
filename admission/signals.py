from django.dispatch import receiver
from admission.utils.application_perms import set_permissions_based_on_application_status
from .models.application import Application
from django.db.models.signals import (
    pre_save,
)

@receiver(pre_save, sender=Application)
def before_instance_is_saved(sender, instance, **kwargs):
    
    if not instance._state.adding:
        set_permissions_based_on_application_status(instance)