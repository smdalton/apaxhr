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


class Passport(models.Model):
    owner = models.OneToOneField(Employee, on_delete=models.CASCADE)

    issue_date = models.DateField(blank=False)
    expiration_date = models.DateField(blank=False)
    dob = models.DateField()
    "https://pypi.org/project/django-countries/"
    #place_of_issue = CountryField(blank=False,null=True)
    place_of_issue = models.CharField(_("Country code as displayed in passport"),max_length=5)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='passports')

    def __str__(self):
        return f"Employee: {self.owner.first_name}"


class WorkPermit(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    valid = models.BooleanField(default=False)
    expiration = models.DateField(blank=False)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='work_permit_images', blank=True, null=True)


def default_ros_expiration():
    now = dt.datetime.now()
    return now + timedelta(days=165)

# store this image in the db with a thumbnail as well
class RegistryOfStayForm(models.Model):

    """ Your Address;
        Your Vietnamese cell number;
        Land Owners Name;
        Land Owners Cell number;
        Land Owners email address;
    """
    # expiration is 6 months
    # if address is null then must be flagged
    address = models.CharField(max_length=100,null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    valid = models.BooleanField(default=False)

    # default expiration = today + 6 months from now
    expiration = models.DateField(default=default_ros_expiration, blank=False, null=True)
    issued = models.DateField(blank=False, auto_now_add=False)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='ros_images',blank=False)

    def compute_default_expiration(self):
        return


class Resume(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='resumes', blank=True, null=True)
    added = models.DateField(auto_now_add=True)
# # #TODO delete this test stub
