from django.db import models

# Create your models here.
from .managers import BiweeklyClassManager
from employment.models import SalariedPosition
from django.utils.translation import gettext_lazy as _
from django.db.models import IntegerField, Model, Q
from django.conf import settings
Employee = settings.AUTH_USER_MODEL




class WeekDays(models.IntegerChoices):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    SUNDAY_AM = 8
    UNUSED = 9


class TimeBlocks(models.IntegerChoices):
    BLOCK_1 = 1, _('Block 1 8:00 - 9:30')
    BLOCK_2 = 2, _('Block 2 9:30 - 11:15 ')
    BLOCK_3 = 3, _('Block 3 14:00 - 15:30')
    BLOCK_4 = 4, _('Block 4 15:45 - 17:15')
    BLOCK_5 = 5, _('Block 5 17:30 - 19:00')
    BLOCK_6 = 6, _('Block 6 19:15 - 20:45')


class LearningCenter(models.Model):
    code = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=40, unique=True)
    city = models.CharField(max_length=25)
    address = models.CharField(max_length=100, unique=True)
    tu_fri = (2, 5)

    def query_test(self):
        print('getting tuesday friday classes for center %s', self)
        day_query = Q(day1=self.tu_fri[0]) & Q(day2=self.tu_fri[1]) & Q(block=5) & Q(block=6)
        return BiWeeklyClass.objects.filter(center=self)

    def __str__(self):
        return f" {self.code}"


class CenterTeacher(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['center', 'teacher'], name='teacher_constraint')
        ]

    is_active = models.BooleanField(default=True)  # deactivate to "delete"
    center = models.ForeignKey(LearningCenter, on_delete=models.CASCADE)
    teacher = models.OneToOneField(SalariedPosition, on_delete=models.CASCADE, related_name='teacher_salaries')
    preferred_room = models.SmallIntegerField(default=-1)

    def __str__(self):
        return f"{self.teacher.employee.full_name}"


class CenterRoom(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['center', 'name'], name='room_constraint')
        ]

    center = models.ForeignKey(LearningCenter, on_delete=models.CASCADE)
    name = models.CharField(_('unique room'),
                            default=-1, max_length=12)
    note = models.TextField(_('Note any important details about a room here'), max_length=250)

    def __str__(self):
        return self.name


class BaseEvent(models.Model):
    class Meta:
        abstract = True
        constraints = [
            models.UniqueConstraint(fields=['center', 'block'], name='room_time_constraint')
        ]

    center = models.ForeignKey(LearningCenter, on_delete=models.CASCADE)
    block = models.SmallIntegerField(choices=TimeBlocks.choices)
    room = models.ForeignKey(CenterRoom, on_delete=models.CASCADE)

    other_note = models.TextField(
        _('Fill out this note if you have selected an other type class'),
        max_length=85,
        default='not an other course')
    recurring = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)



class BiWeeklyClass(BaseEvent):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['center', 'room', 'block', 'day1'], name='double_book_day1'),
            models.UniqueConstraint(fields=['center', 'room', 'block', 'day2'], name='double_book_day2'),
                  ]

    day1_teacher = models.ForeignKey(CenterTeacher, on_delete=models.CASCADE, related_name='day1_teacher')
    day2_teacher = models.ForeignKey(CenterTeacher, on_delete=models.CASCADE, related_name='day2_teacher')

    day1 = models.SmallIntegerField(choices=WeekDays.choices, default=9)
    day2 = models.SmallIntegerField(choices=WeekDays.choices, default=9)

    single_day = models.BooleanField(default=False)

    class_title = models.CharField(max_length=25)
    cm = models.CharField(max_length=30, blank=True)
    objects = BiweeklyClassManager()

    def block_display(self):
        return self.get_block_display()


    def __str__(self):
            return f"{self.class_title} Block {self.block_display()} {self.get_day1_display(),self.get_day2_display()} "


    # an event that is added to some kind of schedule
class BaseScheduledEvent(models.Model):
    class Meta:
        abstract = True


# weekly schedule object, built every monday at 8:00pm

# single weekday schedule model for a centers classes
# many ScheduledClasses will point to this Daily Schedule

# Create a live class instance from the class Template


class CenterWeeklySchedule(BaseScheduledEvent):
    center = models.ForeignKey(LearningCenter, on_delete=models.PROTECT)
    week_start = models.DateField(auto_now_add=True)

    # generates a schedule for one week from the day it is ran

    def generate_weekly_schedule(self):
        pass
        # monday center.
        # tuesday
        # wednesday
        # thursday
        # friday
        # saturday
        # sunday


class CenterDailySchedule(BaseScheduledEvent):
    center = models.ForeignKey(LearningCenter, on_delete=models.PROTECT)
    date = models.DateField(default=-1)
    weekday = models.PositiveSmallIntegerField(choices=WeekDays.choices, default=8)
    weekly_schedule = models.ForeignKey(CenterWeeklySchedule, on_delete=models.CASCADE)

    def get_hours_for_center_teachers_this_day(self):
        return -1


class ScheduledClass(BaseScheduledEvent, BiWeeklyClass):
    containing_schedule = models.ForeignKey(CenterDailySchedule, on_delete=models.CASCADE)
