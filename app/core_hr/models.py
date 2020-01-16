from datetime import datetime


from django.db import models
from django.contrib.auth.models import User
from . import database_choices as db_choice
from django_countries.fields import CountryField
from apaxhr.storage_backends import PublicMediaStorage
from users.models import Employee
from apaxhr.storage_backends import PrivateMediaStorage
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import timezone, timedelta
import datetime as dt



class DataCompleteMixin(models.Model):
    class Meta:
        abstract = True

    @property
    def data_complete(self):
        all_fields_filled = all((getattr(self, field.name) for field in self._meta.fields))
        return all_fields_filled


class ExpirationDateMixin(models.Model):
    class Meta:
        abstract = True

    @property
    def expired(self):
        return not (self.expiration_date > datetime.now().date())



# TODO: Passport
class Passport(ExpirationDateMixin, DataCompleteMixin, models.Model):
    owner = models.OneToOneField(Employee, on_delete=models.CASCADE)
    issue_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)

    "https://pypi.org/project/django-countries/"
    #place_of_issue = CountryField(blank=False,null=True)
    place_of_issue = CountryField(blank_label="select country used in your passport",default='AQ')

    image = models.ImageField(
        storage=PrivateMediaStorage(),
        upload_to='passports',
        blank=True, null=True
                              )

    def __str__(self):
        return f"{self.owner.full_name}"

    @property
    def owners_name(self):
        return self.owner.full_name

    @property
    def employee_number(self):
        return self.owner.employee_id_number


# actual default is 180 days, 170 is for a 10 day warning reminder
def default_ros_expiration(expiration_period=170):
    now = dt.datetime.now()
    return now + timedelta(days=expiration_period)

# Todo ROS form

class RegistryOfStay(ExpirationDateMixin, DataCompleteMixin, models.Model):

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


#Default work permit issue time is 2 years or 730 days, I have set
def default_work_permit_expiration(expiration_period=680):
    return dt.datetime.now().date()+timedelta(days=expiration_period)



class WorkPermit(ExpirationDateMixin, DataCompleteMixin, models.Model):
    kinds = (('wp','Work Permit'),('vs','visa'))
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    expiration_date = models.DateField(default=default_work_permit_expiration, blank=False)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='work_permit_images', blank=True, null=True)

    @property
    def expired(self):
        return dt.datetime.now().date() > self.expiration_date


class Resume(DataCompleteMixin, models.Model):
    choices = (('rs','Resume'),('cv','Curriculum Vitae'))
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type =  models.CharField(max_length=20,choices=choices)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='resumes', blank=True, null=True)
    added = models.DateField(auto_now_add=True)
# # #TODO delete this test stub


class AchievementCertificate(DataCompleteMixin, models.Model):
    help = "Store information for KPI and FAS certificates of achievement"
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='kpi_certificates', blank=False)
    message_text = models.TextField(_('Enter award message for email here'), max_length=1000, blank=False)


class TeachingCertificate(DataCompleteMixin, models.Model):
    certificate_choices = (('c', 'CELTA'), ('ts', 'TESOL'), ('tf', 'TEFL'), ('ot', 'other'))
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=100)
    type  = models.CharField(max_length=15, choices=certificate_choices, blank=True, null=True)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='tefl_certs', blank=False)
    added = models.DateField(auto_now_add=True)

class DegreeDocument(DataCompleteMixin, models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pass

