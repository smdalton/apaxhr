from django.db import models
from django.contrib.auth.models import User
import uuid
from django_countries.fields import CountryField
# Create your models here.
from . import database_choices as db_choice


class PublicImage(models.Model):
    title = models.TextField(max_length=25)
    image = models.ImageField(upload_to='media/profile_pictures', blank=False)
    pass

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='media/profile_pictures', blank=False)
    fname = models.CharField(max_length=25, blank=False)
    mname = models.CharField(max_length=25, blank=False)
    lname = models.CharField(max_length=25, blank=False)
    bio = models.TextField(max_length=1000, blank=False)
    role = models.CharField(
        max_length=50,
        choices=db_choice.roles
    )

    def __str__(self):
        return self.fname + ' ' + self.lname

class DocumentationInfo(models.Model):
    related_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_permit_valid = models.BooleanField(blank=True,default=False)
    passport_valid = models.BooleanField(blank=True, default=False)
    registry_of_stay_valid = models.BooleanField(blank=True, default=False)

    def get_passport_validity(self):
        return False

    def get_registry_of_stay_validity(self):
        return False

    def get_work_permit_validity(self):
        return False

    def get_validity_of_all_documents(self):
        return False


# store this image in the db with a thumbnail as well
class Passport(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    expiration_date = models.DateTimeField(blank=False)
    issue_date = models.DateTimeField(blank=False)


    def get_image(self):
        image = None
        return image

    def expiring_soon(self):
        result = True
        return result


# store this image in the db with a thumbnail as well
class WorkPermit(models.Model):

    pass

# store this image in the db with a thumbnail as well
class RegistryOfStayForm(models.Model):

    pass

class DocumentImage(models.Model):

    pass

#TODO delete this test stub
