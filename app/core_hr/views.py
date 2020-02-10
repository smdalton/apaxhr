from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from users.models import Employee
from django.contrib import messages


class EmployeePortal(TemplateView):
    template_name = 'core-hr/employee-self-service.html'
    try:
        dummy_user = Employee.objects.get(id=4)
    except:
        dummy_user = ""

    def get_context_data(self, **kwargs):
        context = super(EmployeePortal, self).get_context_data()
        try:
            context['documents'] = self.dummy_user.get_document_set()
        except:
            context['documents'] = "none"

        return context

class DocumentCenter(TemplateView):
    template_name = 'core-hr/employee-documents.html'
    try:
        dummy_user = Employee.objects.get(id=4)
    except:
        dummy_user = ""

    def get_context_data(self, **kwargs):
        context = super(DocumentCenter, self).get_context_data()
        try:
            context['documents'] = self.dummy_user.get_document_set()
        except:
            context['documents'] = "none"

        return context


