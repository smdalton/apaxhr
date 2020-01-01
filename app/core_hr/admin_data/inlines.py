from core_hr import models
from django.contrib import admin


class PassportInline(admin.StackedInline):
    model = models.Passport

class WorkPermitInline(admin.StackedInline):
    model = models.WorkPermit

class RegistryOfStayInline(admin.TabularInline):
    model = models.RegistryOfStayForm
