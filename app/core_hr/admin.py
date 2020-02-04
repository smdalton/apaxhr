from datetime import datetime, timedelta

from botocore.exceptions import EndpointConnectionError
from django.contrib import admin

from django.apps import apps
from django.contrib.admin import SimpleListFilter
from django.db.models import Subquery
from django.utils.safestring import mark_safe

import datedelta
from . import models
from .admin_data import inlines
from core_hr.models import Employee, Passport, RegistryOfStay, WorkPermit

class PassportStatusFilter(SimpleListFilter):
    title='Passport Status'
    parameter_name = 'documents'

    def lookups(self, request, model_admin):
        return[

            ('expiring', 'Expires w/in 2mo'),
            ('expired', 'Passport is Expired'),
        ]

    def queryset(self, request, queryset):
        # Employee.objects.filter(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
        if self.value() == 'complete':
            return queryset.filter(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
        elif self.value() == 'not_complete':
            return queryset.exclude(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
        elif self.value() == 'expiring':
            # get all passports that are expiring in the next 3 months
            # get datetime.day for 3 months from now:

            now = datetime.now().date()
            expiring_in_two_months = now + datedelta.datedelta(months=2)
            return queryset.filter(passport__expiration_date__range=[now, expiring_in_two_months])
        elif self.value() == 'expired':
            now = datetime.now().date() - timedelta(days=1)
            past= now - timedelta(days=30000)
            return queryset.filter(passport__expiration_date__range=[past,now])
        else:
            return queryset

class RegistryOfStayStatusFilter(SimpleListFilter):
    title='ROS Status'
    parameter_name = 'ros-status'

    def lookups(self, request, model_admin):
        return[
            ('complete','ROS Complete'),
            ('not_complete', 'ROS Not Complete'),
            ('expiring_soon', 'ROS expiring w/in 2 weeks')
        ]

    def queryset(self, request, queryset):

        if self.value() == 'complete':
            return queryset.filter(pk__in=Subquery(RegistryOfStay.objects.all().values('owner__pk')))
        elif self.value() == 'not_complete':
            return queryset.exclude(pk__in=Subquery(RegistryOfStay.objects.all().values('owner__pk')))
        elif self.value() == 'expiring_soon':
            now = datetime.now().date()
            expiring_in_two_weeks = now + datedelta.datedelta(days=14)
            return queryset.filter(expiration_date__range=[now, expiring_in_two_weeks])

class WorkPermitStatusFilter(SimpleListFilter):
    title='Work Permit Status'
    parameter_name = 'documents'

    def lookups(self, request, model_admin):
        return[
            ('complete','Work Permit Input Complete'),
            ('not_complete', 'Work Permit Input not complete'),
            ('expiring_soon', 'Work Permit/Visa exp. w/in 1 month')
        ]

    def queryset(self, request, queryset):


        if self.value() == 'complete':
            return queryset.filter(pk__in=Subquery(WorkPermit.objects.all().values('owner__pk')))
        elif self.value() == 'not_complete':
            return queryset.exclude(pk__in=Subquery(WorkPermit.objects.all().values('owner__pk')))
        elif self.value() == 'expiring_soon':
            now = datetime.now().date()
            expiring_in_one_month = now + datedelta.datedelta(days=14)
            return queryset.filter(expiration_date__range=[now, expiring_in_one_month])


@admin.register(WorkPermit)
class WorkPermitAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Work Permits'
    model = WorkPermit
    list_display = ('owners_name', 'type', 'expiration_date', 'owners_id', '__str__')
    list_filter = ('expiration_date',)

    search_fields = ('owner__full_name', 'owner__employee_id_number')
    ordering = ('expiration_date',)

    readonly_fields = ['owner', 'document_image']
    def expired(self, obj):
        return obj.expiration_date > datetime.now().date()

    def document_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=obj.image.width / 4,
                height=obj.image.height / 4,
            )
        )


@admin.register(RegistryOfStay)
class RegistryOfStayAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Registry of Stay Forms'
    model = RegistryOfStay
    search_fields = ('owner__full_name', 'owner__employee_id_number')
    ordering = ('expiration_date',)
    readonly_fields = ['owner', 'document_image']
    list_filter = (RegistryOfStayStatusFilter,'expiration_date',)
    def document_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=obj.image.width / 4,
                height=obj.image.height / 4,
            )
        )


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    model = Passport
    search_fields = ('owner__full_name', 'owner__employee_id_number')
    autocomplete_fields = ('owner',)
    list_display = [ 'owners_name', 'expiration_date', 'expired',  'data_complete', 'employee_number', ]
    ordering = ('expiration_date',)

    readonly_fields = ['owner', 'document_image']
    list_filter = (PassportStatusFilter,'expiration_date')

    def document_image(self, obj):
        try:
            return mark_safe(
                '<img src="{url}" width="{width}" height={height} />'.format(
                    url=obj.image.url,
                    width=obj.image.width / 4,
                    height=obj.image.height / 4,
                )
            )
        except EndpointConnectionError as e:
            return mark_safe(f"'<h4>{e}</h4>")


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
