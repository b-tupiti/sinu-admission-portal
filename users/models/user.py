from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from users.manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User
    """
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    middle_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    gender = models.CharField(max_length=1,choices=(('m', 'Male'), ('f', 'Female')),null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Date of Birth', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)