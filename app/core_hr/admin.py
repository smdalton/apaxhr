from django.contrib import admin

from django.apps import apps
from . import models
from .admin_data import inlines
from core_hr.models import Employee, Passport

#
# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     search_fields = ('fname',)
#     list_display = ['fname']

@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    model = Passport
    search_fields = ('owner__full_name', 'owner__employee_id_number')
    autocomplete_fields = ('owner',)
    list_display = ['owners_name','data_complete','expired','employee_number',]




#
# class EmployeeAdmin(ModelAdmin):
#     model = models.Employee
#     fields = ['middle_name','bio','employee_role']
#     search_fields = ['user__first_name','user__last_name','middle_name']
#     inlines= [
#         inlines.PassportInline,
#         #inlines.WorkPermitInline,
#         #inlines.RegistryOfStayInline
#     ]

# admin.site.register(models.Employee, EmployeeAdmin)



#
# hr_models.Passport
#
# hr_models.DocumentationInfo
#
# hr_models.DocumentImage
#
# hr_models.PublicImage
#
# hr_models.RegistryOfStayForm
#
# hr_models.RegistryOfStayForm
#
# hr_models.WorkPermit