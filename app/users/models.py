from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# from core_hr.models import Passport, RegistryOfStay
from .managers import CustomUserManager
from apaxhr.storage_backends import PublicMediaStorage, PrivateMediaStorage
from django.core.validators import RegexValidator

name_validator = RegexValidator(r'^[a-z A-Z]*$', 'Only Alphabetic characters allowed')


# Make Proxy models for different admin interfaces

"""Core Info:
Employment Status: Applicant/Initial Training/Active/Pause **New Field Suggestion**
Employment Status Note
Full Name First, Middle, Last
Gender
Employee ID Code
Apax email
Personal Email	
Phone Number
"""


class Employee(AbstractBaseUser, PermissionsMixin):

    employment_statuses = (
        ('ap','Applicant'),
        ('trial', 'Initial Training'),
        ('em', 'Employed'),
        ('ps','Pause')
    )
    genders = (('M', 'male'),('F', 'female'))
    # core information
    full_name = models.CharField(_('Name as on Passport'), validators=[name_validator], max_length=25, blank=False, null=True)

    #employment data
    gender = models.CharField(max_length=10, choices=genders)
    employee_id_number = models.CharField(_('employee id number'), max_length=20, null=True)

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

    def test_passports(self):
        from core_hr.models import Passport
        owners_passport = Passport.objects.get(owner__pk=self.id)
        if owners_passport.image == None:
            print('image is none')

    def get_contact_info(self):
        try:
            return f"{self.phone_number}, {self.email}, {self.personal_email}"
        except:
            return "Error during retrieval of contact info, perhaps it isn't complete"

    @property
    def passport_complete(self):
        from core_hr.models import Passport
        try:
            passport = self.passport
            return passport.data_complete
        except ObjectDoesNotExist:
            return ["Couldn't query passport, perhaps it was not created?", False]

    @property
    def ros_form_complete(self):
        from core_hr.models import RegistryOfStay
        try:
            ros_form = RegistryOfStay.objects.get(owner=self)
            return ros_form.data_complete
        except ObjectDoesNotExist:
            return ["Couldn't query Registry of stay, perhaps it was not created", False]
        pass


    @property
    def documents_complete(self):
        completion_statuses = [self.passport_complete, self.ros_form_complete]
        return  False if False in completion_statuses else True


    def first_name(self):
        try:
            return str(self.full_name.split()[1])
        except:
            pass
    def middle_name(self):
        try:
            return str(self.full_name.split()[2])
        except:
            pass
    def last_name(self):
        try:
            return str(self.full_name.split()[0])
        except:
            pass

    def __str__(self):
        return f"{self.full_name} {self.email}"


class EmployeeProfile(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    img = models.ImageField(_('Upload Profile Image'), upload_to='profile_images')
    bio = models.TextField(_('Personal Biography'), max_length=500, blank=True, null=True)

