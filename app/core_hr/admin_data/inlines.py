from core_hr import models
from django.contrib import admin


class PassportInline(admin.TabularInline):
    model = models.Passport

class WorkPermitInline(admin.TabularInline):
    model = models.WorkPermit

class RegistryOfStayInline(admin.TabularInline):
    model = models.RegistryOfStayForm
