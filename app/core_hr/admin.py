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
from core_hr.models import Employee, Passport, RegistryOfStay, WorkPermit, DegreeDocument, AchievementCertificate, \
    TeachingCertificate, Resume


class WorkPermitStatusFilter(SimpleListFilter):
    title='Work Permit Status'
    parameter_name = 'documents'

    def lookups(self, request, model_admin):
        return[
            ('not_complete', 'Work Permit Input not complete'),
            ('expiring_soon', 'Work Permit/Visa exp. w/in 1 month'),
            ('expired', 'Work Permit/Visa expired')
        ]

    def queryset(self, request, queryset):



        if self.value() == 'not_complete':
            return queryset.exclude(pk__in=Subquery(WorkPermit.objects.all().values('owner__pk')))
        elif self.value() == 'expiring_soon':
            now = datetime.now().date()
            expiring_in_one_month = now + datedelta.datedelta(days=14)
            return queryset.filter(expiration_date__range=[now, expiring_in_one_month])
        # elif self.value() =='expiring_soon':

class LegalDocumentAdminMixin(object):
    class Meta:
        abstract = True
    ordering = ('expiration_date',)
    list_filter = ('expiration_date',)
    list_display = ('owner', 'expiration_date', 'valid', )
    search_fields = ('owner__full_name', 'owner__employee_id_number')
    readonly_fields = ('owner', 'document_image',)

    def valid(self, obj):
        return obj.expiration_date > datetime.now().date()


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

@admin.register(WorkPermit)
class WorkPermitAdmin(LegalDocumentAdminMixin, admin.ModelAdmin):
    verbose_name_plural = 'Work Permits'
    model = WorkPermit

class RegistryOfStayStatusFilter(SimpleListFilter):
    title='ROS Status'
    parameter_name = 'ros-status'

    def lookups(self, request, model_admin):
        return[

            ('not_complete', 'Not Complete'),
            ('expiring_soon', 'expiring w/in 2 weeks'),
            ('expired', 'expired')
        ]

    def queryset(self, request, queryset):

        if self.value() == 'not_complete':
            return queryset.exclude(pk__in=Subquery(RegistryOfStay.objects.all().values('owner__pk')))
        elif self.value() == 'expiring_soon':
            now = datetime.now().date()
            expiring_in_two_weeks = now + datedelta.datedelta(days=14)
            return queryset.filter(expiration_date__range=[now, expiring_in_two_weeks])
        elif self.value() == 'expired':
            return queryset.filter(expiration_date__lte=datetime.now().date())

@admin.register(RegistryOfStay)
class RegistryOfStayAdmin(LegalDocumentAdminMixin, admin.ModelAdmin):
    model = RegistryOfStay


class PassportStatusFilter(SimpleListFilter):
    title='Passport Status'
    parameter_name = 'documents'

    def lookups(self, request, model_admin):
        return[
            ('expired', 'Expiring'),
            ('expiring', 'Expires w/in 2mo'),
            ('expired', 'Passport is Expired'),
        ]

    def queryset(self, request, queryset):
        # Employee.objects.filter(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
        if self.value() == 'expiring':
            return queryset.filter(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
        elif self.value() == 'expired':
            return queryset.exclude(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
        elif self.value() == 'expiring_soon':
            now = datetime.now().date()
            expiring_in_two_weeks = now + datedelta.datedelta(days=14)
            return queryset.filter(expiration_date__range=[now,expiring_in_two_weeks])
        else:
            return queryset

@admin.register(Passport)
class PassportAdmin(LegalDocumentAdminMixin, admin.ModelAdmin):
    model = Passport
    autocomplete_fields = ('owner',)

class BaseDocumentAdminMixin(object):
    class Meta:
        abstract = True
    list_display = ('owner','date_added')
    search_fields = ('owner__full_name', 'owner__employee_id_number')
    autocomplete_fields = ('owner',)


@admin.register(Resume)
class ResumeAdmin(BaseDocumentAdminMixin, admin.ModelAdmin):
    model = Resume
    verbose_name_plural =  u"\u200B" + 'Resumes'


@admin.register(AchievementCertificate)
class AchievementCertificateAdmin(BaseDocumentAdminMixin, admin.ModelAdmin):
    model= AchievementCertificate
    verbose_name=  u"\u200B" + 'FAS/KPI Achievement Certs'


@admin.register(TeachingCertificate)
class TeachingCertificateAdmin(BaseDocumentAdminMixin, admin.ModelAdmin):
    model = TeachingCertificate
    verbose_name_plural =  u"\u200B" + 'TEFL/CELTA/TESOL etc. Certs.'



@admin.register(DegreeDocument)
class DegreeDocumentAdmin(BaseDocumentAdminMixin, admin.ModelAdmin):
    model = DegreeDocument

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
