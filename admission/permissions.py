from guardian.shortcuts import remove_perm, assign_perm
from django.contrib.auth.models import Group

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

        