from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Employee


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Employee
    list_display = ('email','first_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff','is_active',)

    fieldsets = (
        ('Credentials', {'fields': (('email', 'password',),)}),
        ('Permissions', {'fields': (('is_staff', 'is_active',),)}),
        ('Name',{'fields':('first_name','middle_name','last_name',)}),
        ('Bio',{'fields':('bio',)}),
    )
    add_fieldsets = (
        ('Unknown', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),

        }
         ),
    )

    search_fields = ('email','first_name','last_name')
    ordering = ('email',)


admin.site.register(Employee, CustomUserAdmin)
