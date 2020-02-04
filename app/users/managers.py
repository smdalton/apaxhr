from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _



"""
https://testdriven.io/blog/django-custom-user-model/
"""

class CustomUserManager(BaseUserManager):
    """
    Custom User model with email as unique identifier
    for authentication
    instead of default username
    """
    use_for_related_fields = True

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


    def has_passport(self, **kwargs):
        try:
            print(arg for arg in kwargs.keys())
        except:
            print('nothing in employee has passport manager args')

        return self.all()


    def has_valid_ros(self, **kwargs):
        try:
            print(arg for arg in kwargs.keys())
        except:
            print('nothing in employee has passport manager args')

        return self.all()

    def has_valid_work_permit(self, **kwargs):
        try:
            print(arg for arg in kwargs.keys())
        except:
            print('nothing in employee work permit manager args')

        return self.all()


    def has_resume(self, **kwargs):
        try:
            print(arg for arg in kwargs.keys())
        except:
            print('nothing in employee has passport manager args')

        return self.all()


    def has_teaching_certificate(self, **kwargs):
        try:
            print(arg for arg in kwargs.keys())
        except:
            print('nothing in employee has passport manager args')

        return self.all()


    def has_degree(self, **kwargs):
        try:
            print(arg for arg in kwargs.keys())
        except:
            print('nothing in employee has passport manager args')

        return self.all()



    # from core_hr.models import Passport, RegistryOfStay, WorkPermit
    # ros_forms = RegistryOfStay.objects.all()
    # work_permit = WorkPermit.objects.all()
    # passport_id_set = passports.distinct()
