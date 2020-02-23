from django.db import models

# Create your models here.


class EmployementInfo(models.Model):
    employment_statuses = (
        ('ap', 'Applicant'),
        ('trial', 'Initial Training'),
        ('em', 'Employed'),
        ('ps', 'Pause')
    )

    employment_status = models.CharField(choices=employment_statuses, max_length=30)
    employment_status_note = models.TextField(max_length=500)


class EmployeePosition(models.Model):

    pass


class EmployeePlacement(models.Model):
    pass

