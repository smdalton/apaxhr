from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from . import database_choices as db_choice
from users.models import Employee
from apaxhr.storage_backends import PrivateMediaStorage
from apaxhr.storage_backends import PublicMediaStorage

# Employee = get_user_model()


class Passport(models.Model):
    owner = models.OneToOneField(Employee, on_delete=models.CASCADE)
    expiration_date = models.DateField(blank=False)
    dob = models.DateField()
    issue_date = models.DateField(blank=False)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='passports')

    # profile_picture = hr_models.ImageField(null=True, upload_to='media/profile_pictures', blank=False)

    def __str__(self):
        return f"Employee: {self.owner.first_name}"


class WorkPermit(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    valid = models.BooleanField(default=False)

    expiration = models.DateField(blank=False)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='work_permit_images', blank=True, null=True)


# store this image in the db with a thumbnail as well
class RegistryOfStayForm(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    valid = models.BooleanField(default=False)

    expiration = models.DateField(blank=True, null=True)
    issued = models.DateField(blank=False, auto_now_add=False)

    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='ros_images',blank=False)

class Resume(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    image = models.ImageField(storage=PrivateMediaStorage(), upload_to='resumes', blank=True, null=True)
    added = models.DateField(auto_now_add=True)
# # #TODO delete this test stub
