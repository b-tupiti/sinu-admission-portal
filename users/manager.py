from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):

  def _create_user(
    self, 
    email, 
    password, 
    is_staff, 
    is_superuser, 
    first_name=None, 
    middle_name=None, 
    last_name=None, 
    gender=None, 
    date_of_birth=None, 
    **extra_fields
    ):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        gender=gender,
        date_of_birth=date_of_birth,
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(
    self, 
    email, 
    password, 
    first_name, 
    middle_name, 
    last_name, 
    gender,
    date_of_birth,
    **extra_fields
    ):
    return self._create_user(
      email, 
      password, 
      False, 
      False,
      first_name, 
      middle_name, 
      last_name, 
      gender,
      date_of_birth, 
      **extra_fields
    )

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    return user