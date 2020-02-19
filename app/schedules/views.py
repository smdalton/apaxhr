from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class SchedulesHome(TemplateView):
    template_name = 'schedules/schedules_home.html'


from django.shortcuts import render

# Create your views here.
