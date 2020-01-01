from django.contrib import admin
from django.apps import apps
from . import models
from .admin_data import inlines
# Register your models here.

#
# @admin.register(models.Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     search_fields = ('fname',)
#     list_display = ['fname']
#
# @admin.register(models.Passport)
# class PassportAdmin(admin.ModelAdmin):
#     autocomplete_fields = ('owner',)


class EmployeeAdmin(admin.ModelAdmin):
    model = models.Employee
    fields = ['middle_name','bio','employee_role']
    search_fields = ['user__first_name','user__last_name','middle_name']
    inlines= [
        inlines.PassportInline,
        inlines.WorkPermitInline,
        inlines.RegistryOfStayInline
    ]

admin.site.register(models.Employee, EmployeeAdmin)

    #

#
# models.Passport
#
# models.DocumentationInfo
#
# models.DocumentImage
#
# models.PublicImage
#
# models.RegistryOfStayForm
#
# models.RegistryOfStayForm
#
# models.WorkPermit