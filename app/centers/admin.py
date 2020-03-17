from django.conf import settings
from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from guardian.admin import GuardedModelAdmin
# Register your models here.
from ahr_extras.permissions import DefaultPermissionsMixin
from centers.models import LearningCenter, CenterRoom, CenterTeacher, BiWeeklyClass
from core_hr.extras.dummy import get_dummy_user
from employment.models import SalariedPosition

class LCPermissionsMixin(DefaultPermissionsMixin):
    perms_list = ['Head Teachers', 'Area Managers', 'Faculty Managers', '']


@admin.register(LearningCenter)
class LearningCenterAdmin(LCPermissionsMixin):
    model = LearningCenter
    search_fields = ('name','code')
    verbose_name_plural =  u"\u200B" + 'Learning Centers'


@admin.register(CenterRoom)
class CenterRoomAdmin(LCPermissionsMixin):
    search_fields = ('name',)
    list_filter = ('center__code',)
    ordering = ('name',)
    model = CenterRoom
    verbose_name_plural =  u"\u200B" + 'Center Rooms'

    # BiWeeklyClass.objects.filter(day1_teacher__employee.name)
    def get_queryset(self, request):
        # return the request for a specific user here
        return CenterRoom.objects.filter(center=request.user.get_current_center())

@admin.register(CenterTeacher)
class CenterTeacherAdmin(LCPermissionsMixin):
    search_fields = ('teacher__employee__full_name',)
    model = CenterTeacher
    verbose_name_plural = u"\u200B" + 'Center Teachers'
    list_filter = ('center',)

    autocomplete_fields = ('center',)
    def get_queryset(self, request):
        # return the request for a specific user here
        return CenterTeacher.objects.filter(center=request.user.get_current_center())




@admin.register(BiWeeklyClass)
class BiWeeklyClassAdmin(LCPermissionsMixin):
    model = BiWeeklyClass
    list_display = ('block','room','class_title','day1_teacher','day2_teacher','is_active',)
    list_display_links = None
    autocomplete_fields = ('day1_teacher','day2_teacher')
    list_editable =('block','day1_teacher','day2_teacher',)
    exclude = ('center',)
    list_filter = ( 'is_active','block','day1','day2','class_title',)

    if settings.DEBUG:
        list_per_page = 40
    else:
        list_per_page = 14

    list_select_related = (
        'day1_teacher__teacher',
        'day2_teacher__teacher',
        'day1_teacher__teacher__employee',
        'day2_teacher__teacher__employee',
        'room'
    )


    def change_view(self, request, object_id, form_url='', extra_context=None):
        try:
            return super().change_view(request, object_id, form_url, extra_context)
        except Exception as e:
            print(e)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # print(self.request.user)
        # self.request.user = get_dummy_user()
        center = request.user.get_current_center().pk
        self.center = center
        if db_field.name == "room":
            kwargs["queryset"] = CenterRoom.objects.filter(
                center_id=center
            )
        if db_field.name == "day1_teacher":
            kwargs["queryset"] =CenterTeacher.objects.filter(
                center_id=center
            )
        if db_field.name == "day2_teacher":
            kwargs["queryset"] = CenterTeacher.objects.filter(
                center_id=center
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    verbose_name_plural = u"\u200B" + 'Center Teachers'


    def get_queryset(self, request):
        # return the request for a specific user here
        self.request = request
        queryset = super(BiWeeklyClassAdmin, self).get_queryset(self.request)
        queryset.filter(center=self.request.user.get_current_center())
        # select_related('day1_teacher__teacher__employee','day2_teacher__teacher__employee','room')
        return queryset

            # prefetch_related('day1_teacher__teacher__employee','day2_teacher__teacher__employee','room',)


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
