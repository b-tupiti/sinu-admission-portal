from admission.models.application import Application, ApplicationStatus
from admission.permissions import ObjectPermissionsManager
from django.contrib.auth.models import Group

def set_permissions_based_on_application_status(instance):
    
    original_instance = Application.objects.get(id=instance.id)
    obj_perm_manager = ObjectPermissionsManager(instance)
    
    if original_instance.application_status != instance.application_status:
        obj_perm_manager.remove_all_group_permissions()

        perms = [
                f'view_{instance.__class__._meta.model_name}',
                f'change_{instance.__class__._meta.model_name}',
            ]
        
        if instance.application_status == ApplicationStatus.PENDING_DEPOSIT_VERIFICATION:
            
            group, created = Group.objects.get_or_create(name='Finance')
            groups = [group.name]
            obj_perm_manager.assign_group_permissions(perms, groups)
            
        elif instance.application_status == ApplicationStatus.UNDER_ASSESSMENT:
            
            group, created = Group.objects.get_or_create(name='SAS (Student Administration Services)')
            groups = [group.name]
            obj_perm_manager.assign_group_permissions(perms, groups)