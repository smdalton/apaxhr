from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class SchedulesHomePageView(TemplateView):
    template_name = 'schedules/schedules-home.html'