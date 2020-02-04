from datetime import datetime

from django.contrib import admin

from django.apps import apps
from django.utils.safestring import mark_safe

from . import models
from .admin_data import inlines
from core_hr.models import Employee, Passport, RegistryOfStay, WorkPermit



@admin.register(WorkPermit)
class WorkPermitAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Work Permits'
    model = WorkPermit
    list_display=('owners_name','type', 'expiration_date','owners_id','__str__')
    list_filter = ('expiration_date',)

    search_fields = ('owner__full_name', 'owner__employee_id_number')
    ordering = ('expiration_date',)
    readonly_fields = ['owner','document_image']

    def expired(self, obj):
        return obj.expiration_date > datetime.now().date()

    def document_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width/4,
            height=obj.image.height/4,
        )
        )


@admin.register(RegistryOfStay)
class RegistryOfStayAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Registry of Stay Forms'
    model = RegistryOfStay
    search_fields = ('owner__full_name', 'owner__employee_id_number')

@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    model = Passport
    search_fields = ('owner__full_name', 'owner__employee_id_number')
    autocomplete_fields = ('owner',)
    list_display = ['issue_date','owners_name','data_complete','expired','employee_number',]


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