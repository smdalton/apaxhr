from django.contrib.auth import views as auth_views
from django.urls import path

from . import views



app_name = 'core_hr'

urlpatterns = [
    path('', views.ApaxHomePageView.as_view(), name='landing'),
]