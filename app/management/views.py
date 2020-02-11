from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.

class ManagementHomePage(TemplateView):
    template_name = 'management/management_home.html'
