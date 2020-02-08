from core_hr import models
from django.contrib import admin


class PassportInline(admin.TabularInline):
    verbose_name_plural = 'Passport'
    max_num = 1
    model = models.Passport

class WorkPermitInline(admin.TabularInline):
    verbose_name_plural = 'Work Permit'
    model = models.WorkPermit
    max_num = 1

class RegistryOfStayInline(admin.TabularInline):
    verbose_name_plural = 'Registry Of Stay'
    model = models.RegistryOfStay
    max_num = 1