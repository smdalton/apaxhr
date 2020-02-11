from django.urls import path, include
from django.conf import settings
from . import views



urlpatterns=[
path('',views.ManagementHomePage.as_view(), name='landing'),
]