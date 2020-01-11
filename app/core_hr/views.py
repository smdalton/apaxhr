from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class ApaxHomePageView(TemplateView):
    template_name = 'apaxhr/home.html'

