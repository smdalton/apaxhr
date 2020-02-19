from datetime import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.admindocs.views import ModelDetailView
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView
from django.views.generic.base import TemplateView
# Create your views here.
from django.shortcuts import render
from django.conf import settings

from core_hr.extras.core_hr_mock_factory import get_mock_photo
from core_hr.models import Passport, WorkPermit, RegistryOfStay, Resume, TeachingCertificate, DegreeDocument
from core_hr.tests.test_resumes import ResumeFormTestCase
from users.models import Employee
from django.contrib import messages

from core_hr.extras.dummy import get_dummy_user

years = [x for x in range(1950, 2040)]
years.reverse()

dob_years = [x for x in range(1950, 2005)]
dob_years.reverse()
wp_years = [x for x in range(2017,2025)]
wp_years.reverse()



class CoreHrHome(TemplateView):
    template_name = 'core_hr/core_hr_home.html'
    dummy_user = get_dummy_user()

    def get_context_data(self, **kwargs):
        context = super(CoreHrHome, self).get_context_data()

        # TODO: Stub that needs replacement when user system is in place
        self.request.user = self.dummy_user
        try:
            context['documents'] = self.dummy_user.get_document_set()
        except:
            context['documents'] = "none"

        return context


class DocumentCenter(TemplateView):
    template_name = 'core_hr/employee_documents.html'


    def get_context_data(self, **kwargs):
        context = super(DocumentCenter, self).get_context_data()
        # TODO: Replace stub for user auth
        self.request.user = get_dummy_user()
        context['legal_documents'] = self.request.user.get_legal_documents()
        print(context['legal_documents'])
        context['other_documents'] = self.request.user.get_other_documents()
        print(context['other_documents'])
        return context



class PassportForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = [
            'issue_date',
            'expiration_date',
            'dob',
            'place_of_issue',
            'image'
        ]

        widgets = {
            'issue_date': forms.SelectDateWidget(years=years),
            'expiration_date': forms.SelectDateWidget(years=years),
            'dob': forms.SelectDateWidget(years=years),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input((Submit('submit', 'Save Passport')))


class PassportUpdateCreate(UpdateView):
    form_class = PassportForm
    template_name = 'core_hr/document_templates/update_document.html'
    success_url = reverse_lazy('core_hr:document_center')

    def get_object(self, *args, **kwargs):
        # TODO: replace this stub with the request.user
        self.access_tier = kwargs.get('access_tier', "access tier not present")
        self.request.user = get_dummy_user()
        try:
            obj = Passport.objects.get(owner__id=self.request.user.pk)
        except :
            return Exception('Passport does not exist')

        return obj


class WorkPermitForm(forms.ModelForm):
    class Meta:
        model = WorkPermit
        fields = [
            'type',
            'issue_date',
            'expiration_date',
            'image'
        ]

        widgets = {
            'issue_date': forms.SelectDateWidget(years=years),
            'expiration_date': forms.SelectDateWidget(years=years)
        }
        print('test')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input((Submit('submit', 'Save Work Permit')))



class WorkPermitUpdateCreate(UpdateView):
    form_class = PassportForm
    template_name = 'core_hr/document_templates/update_document.html'
    success_url = reverse_lazy('core_hr:document_center')

    def get_object(self, *args, **kwargs):
        # TODO: replace this stub with the request.user
        self.access_tier = kwargs.get('access_tier', "access tier not present")
        self.request.user = get_dummy_user()
        try:
            obj = Passport.objects.get(owner__id=self.request.user.id)
        except :
            return Exception('Passport does not exist')

        return obj


class ROSForm(forms.ModelForm):
    class Meta:
        model = RegistryOfStay
        fields = [
            'employee_address',
            'landlords_name',
            'landlords_cell_phone',
            'landlords_email',
            'issue_date',
            'expiration_date',
            'image'
        ]
        # this year and next year only
        ros_issue_years = [datetime.now().year-1, datetime.now().year]
        ros_expiration_years = [datetime.now().year]
        widgets = {
            'issue_date': forms.SelectDateWidget(years=ros_issue_years),
            'expiration_date': forms.SelectDateWidget(years=ros_expiration_years),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input((Submit('submit', 'Save ROS')))

class ROSUpdateCreate(UpdateView):
    form_class = ROSForm
    template_name = 'core_hr/document_templates/update_document.html'
    success_url = reverse_lazy('core_hr:document_center')

    def get_object(self, *args, **kwargs):
        # TODO: replace this stub with the request.user
        self.access_tier = kwargs.get('access_tier', "access tier not present")
        self.request.user = get_dummy_user()
        try:
            obj = RegistryOfStay.objects.get(owner=self.request.user)
        except :
            return Exception('Work Permit does not exist')

        return obj


class RosView(DetailView):
    model = RegistryOfStay
    context_object_name = 'ros'
    template_name = 'core_hr/document_templates/view_ros.html'

    def get_object(self, *args, **kwargs):
        self.request.user = get_dummy_user()
        print(self.request.user.pk)
        obj = RegistryOfStay.objects.get(owner=self.request.user)
        if obj.image is None:
            obj.image=get_mock_photo()
        print(obj)
        return obj


class PassportView(DetailView):
    model = Passport
    context_object_name = 'passport'
    template_name = 'core_hr/document_templates/view_passport.html'

    def get_object(self, *args, **kwargs):
        self.request.user = get_dummy_user()
        print(self.request.user.pk)
        obj = Passport.objects.get(owner=self.request.user)
        print(obj)
        return obj

class WorkPermitView(DetailView):
    model = WorkPermit
    context_object_name = 'work_permit'
    template_name = 'core_hr/document_templates/view_work_permit.html'

    def get_object(self, *args, **kwargs):
        self.request.user = get_dummy_user()
        print(self.request.user.pk)
        obj = Passport.objects.get(owner=self.request.user)
        print(obj)
        return obj


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input((Submit('submit', 'Save ROS')))


class ResumeUpdateCreate(UpdateView):
    form_class = ResumeForm
    template_name = 'core_hr/document_templates/..'
    success_url = reverse_lazy('core_hr:resume_update')

    def get_object(self, * args, **kwargs):
        self.access_tier = kwargs.get('access_tier', "Access tier not present")
        #Todo: remove for real auth situations
        self.request.user = get_dummy_user()

### FORM ##
class CertificateForm(forms.ModelForm):
    class Meta:
        model = TeachingCertificate
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input((Submit('submit', 'Save ROS')))


class CertificateUpdateCreate(UpdateView):
    form_class = CertificateForm
    template_name ='core_hr/document_templates/..'
    success_url = reverse_lazy('core_hr:certificate_view')

    def get_object(self, * args, **kwargs):
        self.access_tier = kwargs.get('access_tier', "Access tier not present")
        #Todo: remove for real auth situations
        self.request.user = get_dummy_user()


class DegreeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input((Submit('submit', 'Save ROS')))


class DegreeUpdateCreate(UpdateView):
    form_class = DegreeForm
    template_name ='core_hr/document_templates/..'
    success_url = reverse_lazy('core_hr:degree_view')

    def get_object(self, * args, **kwargs):
        self.access_tier = kwargs.get('access_tier', "Access tier not present")
        #Todo: remove for real auth situations
        self.request.user = get_dummy_user()




class ResumeView(DetailView):
    model = Resume
    context_object_name = 'resume'
    template_name= 'core_hr/document_templates/view_resume.html'
    def get_object(self, *args, **kwargs):
        #TODO remove for real auth situations
        self.request.user= get_dummy_user()
        try:
            obj = Resume.objects.get(owner=self.request.user)
        except:
            return Exception('Document not found')
        return(obj)


class CertificateView(DetailView):
    model = TeachingCertificate
    context_object_name = 'certificate'
    template_name= 'core_hr/document_templates/view_certificate.html'
    def get_object(self, *args, **kwargs):
        #TODO remove for real auth situations
        self.request.user= get_dummy_user()
        try:
            obj = TeachingCertificate.objects.get(owner=self.request.user)
        except:
            return Exception('Document not found')
        return(obj)


class DegreeView(DetailView):
    model = DegreeDocument
    context_object_name = 'degree'
    template_name= 'core_hr/document_templates/view_degree.html'

    def get_object(self, *args, **kwargs):
        #TODO remove for real auth situations
        self.request.user= get_dummy_user()
        try:
            obj = DegreeDocument.objects.get(owner=self.request.user)
        except:
            return Exception('Document not found')
        return(obj)

