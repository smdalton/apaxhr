from django.urls import path, include
from django.conf import settings
from . import views


app_name='management'
urlpatterns=[
path('',views.ManagementHomePage.as_view(), name='landing'),
]