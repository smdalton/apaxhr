from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.
from .models import PublicImage


class BaseView(TemplateView):
    template_name = 'apaxhr/base.html'


def base_template(request):
    return render(request, 'apaxhr/base.html')
