from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from guardian.admin import GuardedModelAdmin
# Register your models here.
from centers.models import LearningCenter, CenterRoom, CenterTeacher, BiWeeklyClass
from core_hr.extras.dummy import get_dummy_user
from employment.models import SalariedPosition


@admin.register(LearningCenter)
class LearningCenterAdmin(GuardedModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    model = LearningCenter
    search_fields = ('name','code')
    verbose_name_plural =  u"\u200B" + 'Learning Centers'


@admin.register(CenterRoom)
class CenterRoomAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    list_filter = ('center__code',)
    ordering = ('name',)
    model = CenterRoom
    verbose_name_plural =  u"\u200B" + 'Center Rooms'
    def get_queryset(self, request):
        # return the request for a specific user here
        return CenterRoom.objects.filter(center__code='HP')

@admin.register(CenterTeacher)
class CenterTeacherAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    model = CenterTeacher
    verbose_name_plural = u"\u200B" + 'Center Teachers'
    list_filter = ('center',)

    autocomplete_fields = ('center',)

#
# class ClassDayFilter(SimpleListFilter):
#     title='Class day pair'
#     parameter_name = 'class_days'
#
#     def lookups(self, request, model_admin):
#         return[
#             ('tu-fri', 'Tue/Fri'),
#             ('wed-sat', 'Wed/Sat'),
#             ('thu-sun', 'Thu/Sa'),
#         ]
#
#     def queryset(self, request, queryset):
#         # Employee.objects.filter(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
#         if self.value() == 'expiring':
#             return queryset.filter(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
#         elif self.value() == 'expired':
#             return queryset.exclude(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
#         elif self.value() == 'expiring_soon':
#             now = datetime.now().date()
#             expiring_in_two_weeks = now + datedelta.datedelta(days=14)
#             return queryset.filter(expiration_date__range=[now,expiring_in_two_weeks])
#         else:
#             return queryset




@admin.register(BiWeeklyClass)
class BiWeeklyClassAdmin(GuardedModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    model = BiWeeklyClass

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(self.request.user)
        self.request.user = get_dummy_user()
        if db_field.name == "room":
            kwargs["queryset"] = CenterRoom.objects.filter(
                center=self.request.user.get_current_center()
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    verbose_name_plural = u"\u200B" + 'Center Teachers'
    list_filter = ('center','block','day1','day2','class_title')
    autocomplete_fields = ('center',)
    def get_queryset(self, request):
        # return the request for a specific user here
        return BiWeeklyClass.objects.filter(center__code='HP')