from django.test import SimpleTestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.urls import resolve

import core_hr.views

import users.views
from . import views


class LandingUrlsResolve(SimpleTestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func.view_class, views.HomePage)

    def test_core_hr_landing_resolves_to_view(self):
        found = resolve('/core_hr')
        self.assertEqual(found.func.view_class, core_hr.views.CoreHrEmployeeHomepage)

    def test_lifecycle_landing_resolves_to_view(self):
        found = resolve('/employee_mgmt')
        self.assertEqual(found.func.view_class, employee_mgmt.views.EmployeeManagementHomePage)

    def test_lifecycle_landing_resolves_to_view(self):
        found = resolve('/employee_mgmt')
        self.assertEqual(found.func.view_class, employee_mgmt.views.EmployeeManagementHomePage)

    def test_users_resolves_to_view(self):
        found = resolve('/users')
        self.assertEqual(found.func.view_class, users.views.UsersHomePage)

#
# class CoreHRUrlsResolve(TestCase):
#
#     def test_core_hr_landing_resolves_to_view(self):
#         pass
#
#     def test_core_hr_landing_resolves_to_view(self):
#         pass
#
#     def test_core_hr_landing_resolves_to_view(self):
#         pass
#
#     def test_core_hr_landing_resolves_to_view(self):
#         pass
#
#     def test_core_hr_landing_resolves_to_view(self):
#         pass
#
#     def test_core_hr_landing_resolves_to_view(self):
#         pass
#
#     def test_core_hr_landing_resolves_to_view(self):
#         pass
#
#     def test_core_hr_landing_resolves_to_view(self):
#         pass
#
#

