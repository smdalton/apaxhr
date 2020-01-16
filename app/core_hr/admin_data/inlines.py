from core_hr import models
from django.contrib import admin


class PassportInline(admin.TabularInline):
    max_num = 1
    model = models.Passport

class WorkPermitInline(admin.TabularInline):
    model = models.WorkPermit
    max_num = 1

class RegistryOfStayInline(admin.TabularInline):
    model = models.RegistryOfStay
    max_num = 1