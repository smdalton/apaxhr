from django.urls import path, include
from django.conf import settings
from . import views

app_name = 'schedules'

urlpatterns = [
    path('', views.SchedulesHome.as_view(), name='landing'),
]