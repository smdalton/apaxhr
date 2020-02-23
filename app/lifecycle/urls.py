from django.urls import path, include
from django.conf import settings
from . import views


app_name='lifecycle'

urlpatterns=[
path('',views.LifeCycleHome.as_view(), name='landing'),
]