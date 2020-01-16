from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Employee
from core_hr.admin_data import inlines


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Employee
    search_fields = ('email','first_name','employee_id_number')
    list_display = ('email','full_name', 'is_active',)
    list_filter = ('employment_status','is_staff','is_active',)

    fieldsets = (
        ('Credentials', {'fields': (('email','personal_email',),)}),
        ('Permissions', {'fields': (('is_staff', 'is_active',),)}),
        ('Name',{'fields':('full_name',)}),
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
