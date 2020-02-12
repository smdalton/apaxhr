from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class EmployeeManagementHomePage(TemplateView):
    template_name = 'employee_mgmt/employee_mgmt_home.html'