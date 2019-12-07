from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Passport(models.Model):
    owner = models.OneToOneField(Employee, on_delete=models.CASCADE)

