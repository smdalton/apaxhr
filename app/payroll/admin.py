from django.contrib import admin

# Register your models here.
from payroll.models import PositionSalaryInfo




@admin.register(PositionSalaryInfo)
class EmployeePositionAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    model = PositionSalaryInfo
    verbose_name_plural =  u"\u200B" + 'PositionSalaryInfo'
