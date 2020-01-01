from django.contrib.auth import views as auth_views
from django.urls import path

from . import views



app_name = 'core_hr'

urlpatterns = [
    path('', views.BaseView.as_view(), name='landing'),
]