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
    title='Passport Complete'
    parameter_name = 'documents'

    def lookups(self, request, model_admin):
        return[
            ('complete','Passport Complete'),
            ('not_complete', 'Not Complete')
        ]

    def queryset(self, request, queryset):
        # Employee.objects.filter(pk__in=Subquery(Passport.objects.all().values('owner__pk')))

        if self.value() == 'complete':
            return queryset.filter(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
        else:
            return queryset.exclude(pk__in=Subquery(Passport.objects.all().values('owner__pk')))

class RegistryOfStayStatusFilter(SimpleListFilter):
    title='Passport Complete'
    parameter_name = 'documents'

    def lookups(self, request, model_admin):
        return[
            ('complete','ROS documentation Complete'),
            ('not_complete', 'ROS documentation Not Complete'),
            ('expiring_soon', 'ROS documentation expiring soon')
        ]

    def queryset(self, request, queryset):


        if self.value() == 'complete':
            return queryset.filter(pk__in=Subquery(RegistryOfStay.objects.all().values('owner__pk')))
        else:
            return queryset.exclude(pk__in=Subquery(RegistryOfStay.objects.all().values('owner__pk')))

# one to one exists filter https://djangosnippets.org/snippets/2591/

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Employee
    search_fields = ('email','full_name','employee_id_number')
    list_display = ('full_name','documents_complete', 'passport','registryofstay')

    list_filter = ('employment_status', 'is_staff', 'is_active', PassportStatusFilter)
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
