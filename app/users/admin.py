from _testcapi import datetime_check_delta
from datetime import datetime, timedelta
import datedelta
from datedelta import datedelta

from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.auth.admin import UserAdmin
from django.db.models import Subquery, Q

from core_hr.models import Passport, RegistryOfStay, WorkPermit
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Employee
from core_hr.admin_data import inlines


# https://timonweb.com/tutorials/adding-custom-filters-to-django-admin-is-easy/


# one to one exists filter https://djangosnippets.org/snippets/2591/


class DocumentCompletionStatusFilter(SimpleListFilter):
    title = 'Document Creation Filter'
    parameter_name = 'completion-info'

    def lookups(self, request, model_admin):
        return [
            ('created', 'Documents created'),
            ('incomplete', 'Documents Incomplete')
        ]

    def queryset(self, request, queryset):
        complex_query = \
            Q(pk__in=Subquery(Passport.objects.all().values('owner__pk')))\
            &Q(pk__in=Subquery(RegistryOfStay.objects.all().values('owner__pk')))\
            &Q(pk__in=Subquery(WorkPermit.objects.all().values('owner__pk')))
        all_created = queryset.filter(complex_query)

        # Subquery(Passport.objects.all().values('owner__pk')
        if self.value() == 'created':
            return all_created
        elif self.value() == 'incomplete':
            return queryset.exclude(complex_query)
        # get all passports that are expiring in the next 3 months
        # get datetime.day for 3 months from now:


class DocumentExpirationStatusFilter(SimpleListFilter):
    title = 'Document Expiration Urgency'
    parameter_name = 'expiration-info'

    def lookups(self, request, model_admin):
        return [
            ('expired', 'Documents are expired'),
            ('expiring_very_soon', 'Documents are expiring w/in 2 weeks'),
            ('expiring_soon', 'Documents are expiring w/in 2 months'),
            ('inactive_users', 'Inactive Users with expired Documents')
        ]

    def queryset(self, request, queryset):

        if self.value() == 'expired':
            return Employee.objects.has_expired_documents()
        elif self.value() == 'expiring_very_soon':
            return Employee.objects.has_documents_expiring_very_soon()
        elif self.value() == 'expiring_soon':
            return Employee.objects.has_documents_expiring_soon()
        elif self.value() == 'inactive_users':
            return Employee.objects.has_expired_documents_inactive()
        else:
            return queryset


class CustomUserAdmin(UserAdmin):
    class Meta:
        verbose_name= 'Employees'

    def has_delete_permission(self, request, obj=None):
        return False

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Employee
    search_fields = ('email','full_name','employee_id_number')
    list_display = ('full_name', 'registryofstay', 'workpermit', 'passport',)

    list_filter = (DocumentExpirationStatusFilter, DocumentCompletionStatusFilter, 'is_active')
    #list_filter = ('employment_status','is_staff', 'is_active')

    fieldsets = (
        ('Credentials', {'fields': (('email','personal_email','is_staff', 'is_active',),)}),
        ('Name',{'fields':('full_name',)}),
        #('Permissions', {'fields': (('is_staff', 'is_active',),)}),
    )

    # add_fieldsets = (
    #     ('Unknown', {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
    #     }
    #      ),
    # )

    inlines = [
        inlines.PassportInline,
        inlines.WorkPermitInline,
        inlines.RegistryOfStayInline
    ]
    ordering = ('email',)



admin.site.register(Employee, CustomUserAdmin)
