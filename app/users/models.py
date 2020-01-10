from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager
from apaxhr.storage_backends import PublicMediaStorage, PrivateMediaStorage
from django.core.validators import RegexValidator

name_validator = RegexValidator(r'^[a-zA-Z]*$', 'Only Alphabetic characters allowed')


# Make Proxy models for different admin interfaces

class Employee(AbstractBaseUser, PermissionsMixin):

    employment_statuses = (
        ('trial', 'Initial Training'),
        ('em', 'Employed'),
        ('ps','pause')
    )
    genders = (('m', 'male'),('f', 'female'))
    # core information
    full_name = models.CharField(_('Full name as on passport'), validators=[name_validator], max_length=25, blank=False, null=True)

    #employment data
    gender = models.CharField(max_length=10, choices=genders)
    employee_id_code = models.IntegerField(_('employee id number'), null=True)

    # activity Status
    employment_status = models.CharField(choices=employment_statuses, max_length=30)
    employment_status_note = models.TextField(max_length=500)



    # contact information
    phone_number = models.CharField(max_length=14, unique=True)
    email = models.EmailField(_('APAX email address'), unique=True)
    personal_email = models.EmailField(_('Personal Email Address'), unique=True)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def first_name(self):
        try:
            return str(self.full_name.split()[0])
        except:
            pass
    def first_name(self):
        try:
            return str(self.full_name.split()[0])
        except:
            pass
    def first_name(self):
        try:
            return str(self.full_name.split()[0])
        except:
            pass
    def __str__(self):
        return self.email

class EmployeeProfile(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    img = models.ImageField(_('Upload Profile Image'), storage=PublicMediaStorage(), upload_to='profile_images')
    bio = models.TextField(_('Personal Biography'), max_length=500, blank=True, null=True)