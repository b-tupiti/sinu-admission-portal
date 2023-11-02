from guardian.shortcuts import remove_perm, assign_perm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test

class ObjectPermissionsManager():
    
    def __init__(self, obj):
        self.model = obj.__class__
        self.obj = obj
        
    def remove_all_group_permissions(self):
        groups = Group.objects.all()
        for group in groups:
            remove_perm(f'view_{self.model._meta.model_name}', group, self.obj)
            remove_perm(f'change_{self.model._meta.model_name}', group, self.obj)
            
    def assign_group_permissions(self, permissions: list[str], groups: list[str]):
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            for perm in permissions:
                assign_perm(perm, group, self.obj)
                
def permission_required(permission_name, login_url=None, raise_exception=False):
    """
    Custom decorator to check for a specific permission.
    :param permission_name: The name of the permission to check.
    :param login_url: URL to redirect to if the user is not authenticated.
    :param raise_exception: If True, raise a PermissionDenied exception on failure.
    """
    def check_permission(user):
        return user.has_perm(permission_name)

    return user_passes_test(
        check_permission,
        login_url=login_url,
        raise_exception=raise_exception
    )

        