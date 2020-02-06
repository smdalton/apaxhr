from datetime import datetime
import datetime as dt

from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import timezone, timedelta
from django.conf import settings
from apaxhr.storage_backends import PublicMediaStorage
Employee = settings.AUTH_USER_MODEL
from apaxhr.storage_backends import PrivateMediaStorage


#Default work permit expiration time is 2 years or 730 days, I have set
def default_work_permit_expiration(expiration_period=680):
    return dt.datetime.now().date()+timedelta(days=expiration_period)

def default_ros_expiration(expiration_period=170):
    now = dt.datetime.now()
    return now + timedelta(days=expiration_period)

class TrackingUtilitiesMixin(models.Model):
    class Meta:
        abstract = True

    verified = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    #email_active = models.BooleanField(default=True)
    @property
    def data_complete(self):
        self.__dict__
        all_fields_filled = all((getattr(self, field.name) for field in self._meta.fields))
        return all([getattr(self, field.name) for field in self._meta.fields])


class ExpirationDateMixin(models.Model):
    class Meta:
        abstract = True

    @property
    def expired(self):
        return dt.datetime.now().date() > self.expiration_date

class LegalDocument(models.Model):
    class Meta:
        abstract = True
    owner = models.OneToOneField(Employee, on_delete=models.CASCADE)
    issue_date = models.DateField(_('Document Date of Issue'),blank=False)
    expiration_date = models.DateField(_('Document Expiration Date'),blank=False, null=False)
    image_dir = 'default_images'
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to=image_dir, blank=False, null=False)


# TODO: Passport
class Passport(ExpirationDateMixin, TrackingUtilitiesMixin, LegalDocument):
    "https://pypi.org/project/django-countries/"
    #place_of_issue = CountryField(blank=False,null=True)
    class Meta:
        verbose_name = 'Passport'
    dob = models.DateField(blank=False, null=False)
    place_of_issue = CountryField(blank_label="select country used in your passport",default='AQ')
    image = models.ImageField(storage=PrivateMediaStorage(),upload_to='passports',blank=False, null=False)


    def __str__(self):
        expiration_data = 'Expired' if self.expired else 'Valid'
        formatted_date = self.expiration_date.strftime("%d-%m-%Y")
        return f"{expiration_data}, exp. date: {formatted_date}"

    @property
    def owners_name(self):
        return self.owner.full_name

    @property
    def employee_number(self):
        return self.owner.employee_id_number


# actual default is 180 days, 170 is for a 10 day warning reminder

class RegistryOfStay(ExpirationDateMixin, TrackingUtilitiesMixin,  LegalDocument):

    """ Your Address;
        Your Vietnamese cell number;
        Land Owners Name;
        Land Owners Cell number;
        Land Owners email address;
    """
    # expiration is 6 months
    # if address is null then must be flagged
    class Meta:
        verbose_name = 'Registry of Stay Form'
    employee_address = models.CharField(max_length=100,blank=False)
    landlords_name = models.CharField(max_length=100,blank=False)
    landlords_cell_phone = models.CharField(max_length=25, blank=False)
    landlords_email = models.EmailField(max_length=25, blank=False)
    image_dir='ros_images'
    image = models.ImageField(
            storage=PrivateMediaStorage(),
            upload_to='ros_images',
            blank=False
    )

    @property
    def phone_number(self):
        return self.owner.phone_number

    def __str__(self):
        expiration_data = 'Expired' if self.expired else 'Valid'
        formatted_date = self.expiration_date.strftime("%d-%m-%Y")
        return f"{expiration_data}, exp. date: {formatted_date}"


class WorkPermit(ExpirationDateMixin, TrackingUtilitiesMixin, LegalDocument):
    class Meta:
        verbose_name ='Work Permit and Visa'
    document_choices = (('wp','Work Permit'),('vs','visa'))
    type = models.CharField(choices=document_choices, blank=False, max_length=2)


    def owners_name(self):
        return self.owner.full_name
    def owners_id(self):
        return self.owner.employee_id_number

    def __str__(self):
        expiration_data = 'Expired' if self.expired else 'Valid'
        formatted_date = self.expiration_date.strftime("%d-%m-%Y")
        return f"{expiration_data}, exp. date: {formatted_date}"


class BaseDocument(TrackingUtilitiesMixin, models.Model):
    class Meta:

        abstract = True
    owner = models.OneToOneField(Employee, on_delete=models.CASCADE)
    image = models.ImageField(
        storage=PrivateMediaStorage(),
        upload_to='base_documents', blank=False, null=False)


class Resume(BaseDocument):
    class Meta:

        verbose_name = u"\u200B" + 'Resume and CV\''
    help = "Stores a resume or CV document"
    document_choices = (('rs','Resume'),('cv','Curriculum Vitae'))
    type =  models.CharField(max_length=20,choices=document_choices)

# # #TODO delete this test stub



class AchievementCertificate(BaseDocument):
    class Meta:
        verbose_name =u"\u200B" + 'FAS/KPI Certificate'
    help = "Store information for KPI and FAS certificates of achievement"
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    image = models.ImageField(
        storage=PrivateMediaStorage(),
        upload_to='kpi_certificates',
        blank=False,
        null=False
    )
    message_text = models.TextField(_('Enter award message for email here'), max_length=1000, blank=False)

class TeachingCertificate(BaseDocument):
    class Meta:
        verbose_name = u"\u200B" + 'TESL/TESOL/CELTA/TEFL etc. certifcates'
    help = "Stores a teaching certificate"
    certificate_choices = (('c', 'CELTA'), ('ts', 'TESOL'), ('tf', 'TEFL'), ('ot', 'other'))
    id_number = models.CharField(max_length=100)
    type  = models.CharField(max_length=15, choices=certificate_choices, blank=False, null=False)
    image = models.ImageField(
        storage=PrivateMediaStorage(),
        upload_to='tefl_certs',
        blank=False,
        null=False
    )

class DegreeDocument(BaseDocument):
    class Meta:
        verbose_name = u"\u200B" + 'Degree Document'
    help = "Stores a College diploma document"
    image = models.ImageField(
        storage=PrivateMediaStorage(),
        upload_to='degree_certs',
        blank=False,
        null=False
    )


