from django.contrib import admin

# Register your models here.
from employment.models import SalariedPosition

#
@admin.register(SalariedPosition)
class EmployeePositionAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    model = SalariedPosition
    # list_filter = ('employee',)
    verbose_name_plural =  u"\u200B" + 'EmployeePosition'
