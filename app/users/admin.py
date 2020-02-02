from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.auth.admin import UserAdmin
from django.db.models import Subquery

from core_hr.models import Passport, RegistryOfStay, WorkPermit
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Employee
from core_hr.admin_data import inlines


# https://timonweb.com/tutorials/adding-custom-filters-to-django-admin-is-easy/
class PassportStatusFilter(SimpleListFilter):
    title='Passport Status'
    parameter_name = 'documents'

    def lookups(self, request, model_admin):
        return[
            ('complete','Passport Complete'),
            ('not_complete', 'Not Complete'),
            ('expiring', 'Passport Expiring Soon')
        ]

    def queryset(self, request, queryset):
        # Employee.objects.filter(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
        if self.value() == 'complete':
            return queryset.filter(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
        elif self.value() == 'not_complete':
            return queryset.exclude(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
        else:
            return queryset

class RegistryOfStayStatusFilter(SimpleListFilter):
    title='ROS Status'
    parameter_name = 'ros-status'

    def lookups(self, request, model_admin):
        return[
            ('complete','ROS Complete'),
            ('not_complete', 'ROS Not Complete'),
            ('expiring_soon', 'ROS expiring soon')
        ]

    def queryset(self, request, queryset):

        if self.value() == 'complete':
            return queryset.filter(pk__in=Subquery(RegistryOfStay.objects.all().values('owner__pk')))
        else:
            return queryset.exclude(pk__in=Subquery(RegistryOfStay.objects.all().values('owner__pk')))


class WorkPermitStatusFilter(SimpleListFilter):
    title='Work Permit Status'
    parameter_name = 'documents'

    def lookups(self, request, model_admin):
        return[
            ('complete','Work Permit Complete'),
            ('not_complete', 'Work Permit not complete'),
            ('expiring_soon', 'Work Permit expiring soon')
        ]

    def queryset(self, request, queryset):


        if self.value() == 'complete':
            return queryset.filter(pk__in=Subquery(WorkPermit.objects.all().values('owner__pk')))
        else:
            return queryset.exclude(pk__in=Subquery(WorkPermit.objects.all().values('owner__pk')))

# one to one exists filter https://djangosnippets.org/snippets/2591/

class CustomUserAdmin(UserAdmin):
    class Meta:
        verbose_name= 'Employees'

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Employee

    search_fields = ('email','full_name','employee_id_number')
    list_display = ('full_name', 'registryofstay', 'workpermit', 'passport',)

    list_filter = (PassportStatusFilter, 'employment_status', 'is_active')
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
