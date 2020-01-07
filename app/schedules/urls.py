from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SchedulesHomePageView.as_view(),name='schedules_homepage'),
    ]