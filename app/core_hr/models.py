from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid
from django_countries.fields import CountryField
# Create your models here.
from . import database_choices as db_choice
import datetime as dt
import django.utils.timezone as tz




class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, blank=False, default='')
    middle_name = models.CharField(max_length=25, blank=False, default='')
    last_name = models.CharField(max_length=25, blank=False, default='')
    bio = models.TextField(max_length=1000, blank=False, default='')
    employee_role = models.CharField(
        max_length=50,
        choices=db_choice.roles,
        default='',
    )
    def get_last_name(self):
        return str(self.user.last_name)

    def __str__(self):
        return f"{self.user.first_name}"
#
# class EmployeeWorkHistory(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     join_date = models.DateTimeField()

class Passport(models.Model):
    owner = models.OneToOneField(Employee, on_delete=models.CASCADE)
    expiration_date = models.DateTimeField(blank=False)
    issue_date = models.DateTimeField(blank=False)
    image = models.ImageField(upload_to='media_images')
    pdf = models.FileField(upload_to='document_images')

    def get_image(self):
        image = None
        return image

    def expiring_soon(self):
        result = True
        return result

    # profile_picture = models.ImageField(null=True, upload_to='media/profile_pictures', blank=False)

    def __str__(self):
        return f"Employee: {self.owner.first_name}"


# store this image in the db with a thumbnail as well

# store this image in the db with a thumbnail as well
#




class PublicImage(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.TextField(max_length=25, default='')
    image = models.ImageField(upload_to='profile_pictures', blank=False, null=True)


class WorkPermit(models.Model):
    owner = models.OneToOneField(Employee, on_delete=models.CASCADE)
    expiration = models.DateTimeField(blank=False)
    pdf = models.FileField(upload_to='document_images',blank=False, null=True)
    image = models.ImageField(upload_to='work_permit_images', blank=True, null=True)


# store this image in the db with a thumbnail as well
class RegistryOfStayForm(models.Model):
    owner = models.OneToOneField(Employee, on_delete=models.CASCADE)
    expiration = models.DateTimeField(blank=False)
    issued = models.DateTimeField(blank=False)
    pdf = models.FileField(upload_to='document_images',blank=False, null=True)


# #TODO delete this test stub
