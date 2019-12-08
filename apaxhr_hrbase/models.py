from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField
# Create your models here.



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_user')
    date_joined = models.DateField(blank=False, auto_now=False)


class Passport(models.Model):
    owner = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='passport_owner')
    expiration = models.DateField()
    home_country = CountryField()

