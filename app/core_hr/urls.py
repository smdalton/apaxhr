from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'core_hr'

urlpatterns = [
    path('', views.CoreHrHome.as_view(), name='self_service'),
    path('documents/', views.DocumentCenter.as_view(), name='document_center'),

    path('documents/passport/view/', views.PassportView.as_view(), name='passport_view'),
    path('documents/passport/update/', views.PassportUpdateCreate.as_view(), name='passport_update'),

    path('documents/ros/view/', views.RosView.as_view(), name='ros_view'),
    path('documents/ros/update/', views.ROSUpdateCreate.as_view(), name='ros_update'),

    path('documents/work_permit/view/', views.WorkPermitView.as_view(), name='work_permit_view'),
    path('document/work_permit/update', views.WorkPermitUpdateCreate.as_view(), name='work_permit_update'),

    path('documents/resume/view/', views.ResumeView.as_view(), name='resume_view'),
    path('documents/resume/update/', views.ResumeUpdateCreate.as_view(), name='resume_update'),

    path('documents/certificate/view/', views.CertificateView.as_view(), name='certificate_view'),
    path('documents/certificate/update/', views.CertificateUpdateCreate.as_view(), name='certificate_update'),

    path('documents/degree/view/', views.DegreeView.as_view(), name='degree_view'),
    path('documents/degree/update/', views.DegreeUpdateCreate.as_view(), name='degree_update'),

]

#
# path('documents/passport/create/', views.PassportUpdate.as_view(), name='passport_create'),
#
# path('documents/passport/view/', views.Detail.as_view(), name='_view'),
# path('documents/passport/update/', views.Update.as_view(), name='_update'),
# path('documents/passport/create/', views.Update.as_view(), name='_create'),
#
# path('documents/passport/view/', views.Detail.as_view(), name='passport_view'),
# path('documents/passport/update/', views.Update.as_view(), name='passport_update'),
# path('documents/passport/create/', views.Update.as_view(), name='passport_create'),
#
# path('documents/passport/view/', views.Detail.as_view(), name='_view'),
# path('documents/passport/update/', views.Update.as_view(), name='_update'),
# path('documents/passport/create/', views.Create.as_view(), name='_create')
