from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from users.models import Employee
from django.contrib import messages




class CoreHrEmployeeHomepage(TemplateView):
    template_name = 'core-hr/core_hr_home.html'
    try:
        dummy_user = Employee.objects.get(id=4)
    except:
        dummy_user = ""

    def get_context_data(self, **kwargs):
        context = super(CoreHrEmployeeHomepage, self).get_context_data()

        # TODO: Stub that needs replacement when user system is in place

        try:
            context['documents'] = self.dummy_user.get_document_set()
        except:
            context['documents'] = "none"

        return context

class DocumentCenter(TemplateView):
    template_name = 'core-hr/employee_documents.html'
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


