from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from . import database_choices as db_choice
from users.models import Employee
from apaxhr.storage_backends import PrivateMediaStorage
from django_countries.fields import CountryField
from apaxhr.storage_backends import PublicMediaStorage
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import timezone, timedelta
import datetime as dt

# Employee = get_user_model()

class DataCompleteMixin(models.Model):
    class Meta:
        abstract = True

    @property
    def data_complete(self):
        all_fields_filled = all((getattr(self, field.name) for field in self._meta.fields))
        return str(all_fields_filled)


class ExpirationDateMixin(models.Model):
    class Meta:
        abstract = True

    @property
    def expired(self):
        return not (self.expiration_date > datetime.now().date())



# TODO: Passport
class Passport(ExpirationDateMixin, DataCompleteMixin,models.Model):
    owner = models.OneToOneField(Employee, on_delete=models.CASCADE)

    issue_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)

    "https://pypi.org/project/django-countries/"
    #place_of_issue = CountryField(blank=False,null=True)
    place_of_issue = models.CharField(
        _("Country code as displayed in passport"),
        max_length=5, blank=True, null=True
    )

    image = models.ImageField(
        storage=PrivateMediaStorage(),
        upload_to='passports',
        blank=True, null=True
                              )

    # @property
    # def data_complete(self):
    #     all_fields_filled = all((getattr(self, field.name) for field in self._meta.fields))
    #     return str(all_fields_filled)

    def __str__(self):
        return f"Employee: {self.owner.full_name}"

    @property
    def owners_name(self):
        return self.owner.full_name

    @property
    def employee_number(self):
        return self.owner.employee_id_number






def default_ros_expiration(expiration_period=680):
    now = dt.datetime.now()
    return now + timedelta(days=expiration_period)

# Todo ROS form

class RegistryOfStayForm(models.Model):

    """ Your Address;
        Your Vietnamese cell number;
        Land Owners Name;
        Land Owners Cell number;
        Land Owners email address;
    """
    # expiration is 6 months
    # if address is null then must be flagged
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    employee_address = models.CharField(max_length=100,blank=True, null=True)
    landlords_name = models.CharField(max_length=100,blank=True, null=False)
    landlords_cell_phone = models.CharField(max_length=25, blank=True, null=True)
    landlords_email = models.EmailField(max_length=25, blank=True, null=True)
    expiration_date = models.DateField(default=default_ros_expiration, blank=True, null=True)

    issued = models.DateField(blank=False, auto_now_add=True)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='ros_images',blank=False)

    @property
    def phone_number(self):
        return self.employee.phone_number

    @property
    def expired(self):
        return dt.datetime.now().date() > self.expiration_date

    @property
    def data_complete(self):
        all_fields_filled = all((getattr(self, field.name) for field in self._meta.fields))
        return str(all_fields_filled)

    @property
    def compute_default_expiration(self):
        return

def default_work_permit_expiration(expiration_period=680):
    return dt.datetime.now().date()+timedelta(days=expiration_period)

class WorkPermit(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    expiration_date = models.DateField(default=default_work_permit_expiration, blank=False)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='work_permit_images', blank=True, null=True)

    @property
    def expired(self):
        return dt.datetime.now().date() > self.expiration_date

    @property
    def data_complete(self):
        all_fields_filled = all((getattr(self, field.name) for field in self._meta.fields))
        return str(all_fields_filled)


#
#
# class Resume(models.Model):
#     owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     image = models.ImageField(storage=PrivateMediaStorage(), upload_to='resumes', blank=True, null=True)
#     added = models.DateField(auto_now_add=True)
# # # #TODO delete this test stub
#
# class AchievementCertificate(models.Model):
#
#     owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     #TODO type =
#     image = models.ImageField(storage=PrivateMediaStorage(), upload_to='kpi_certificates', blank=False)
#     message_text = models.TextField(_('Enter award message for email here'), max_length=1000, blank=False)
#
# class TeflTeachingCertificate(models.Model):
#     owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     image = models.ImageField(storage=PrivateMediaStorage(), upload_to='tefl_certs', blank=False)
#     added = models.DateField(auto_now_add=True)
