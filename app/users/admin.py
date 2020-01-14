from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Employee


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Employee
    search_fields = ('email','first_name','employee_id_number')
    list_display = ('email','full_name', 'is_active',)
    list_filter = ('is_staff','is_active',)

    fieldsets = (
        ('Credentials', {'fields': (('email','personal_email', 'password',),)}),
        ('Permissions', {'fields': (('is_staff', 'is_active',),)}),
        ('Name',{'fields':('full_name',)}),

    )
    add_fieldsets = (
        ('Unknown', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),

        }
         ),
    )

    ordering = ('email',)



admin.site.register(Employee, CustomUserAdmin)
