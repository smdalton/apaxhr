from django.contrib.auth import views as auth_views
from django.urls import path

from . import views



app_name = 'core_hr'

urlpatterns = [
    path('', views.EmployeePortal.as_view(), name='self_service'),
    path('documents/', views.DocumentCenter.as_view(), name='document_center'),


]