from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Upload

class BaseView(TemplateView):
    template_name = 'apaxhr/base.html'


def base_template(request):
    return render(request, 'apaxhr/base.html')


