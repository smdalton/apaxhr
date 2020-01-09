from django.contrib.auth.models import User
from django.forms import SplitDateTimeField
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.urls import resolve
from . import views



class SmokeTest(TestCase):
    def test_math(self):
        self.assertEqual((1+1),2)

class ApaxHomePageTestCase(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func.view_class, views.ApaxHomePageView)


    #
    # def setup(self):
    #     self.fail('Make an employee test case')
    #
    # def test_employee_has_photo_avatar(self):
    #     self.fail('Implement photo checking')


#
# class PassportTestCase(TestCase):
#
#     def setUp(self):
#         self.fail('Make an employee test case')
#
#     def test_passport_exists(self):
#         self.fail('create and check for existence of a passport')
#
#     def test_passport_expired(self):
#         self.fail('create several passports and an expired passport and check for expired passports')
#
#     def test_user_exists(self):
#         self.fail('Make an employee test case')
#
#     # def test_employee_exists(self):
#
#
# class WorkPermitTestCase(TestCase):
#
#     document_name = 'Work Permit'
#     def setUp(self):
#         self.fail('Make an employee test case')
#         self.document_name = 'Work Permit'
#
#     def test_passport_exists(self):
#         self.fail(f"create and check for existence of a {self.document_name}")
#
#     def test_passport_expired(self):
#         self.fail('create several passports and an expired passport and check for expired passports')
#
#     def test_user_exists(self):
#         self.fail('Make an employee test case')
#
#
# class VisaTestCase(TestCase):
#
#     def setUp(self):
#         self.fail('Make an employee test case')
#
#     def test_passport_exists(self):
#         self.fail('create and check for existence of a passport')
#
#     def test_passport_expired(self):
#         self.fail('create several passports and an expired passport and check for expired passports')
#
#     def test_user_exists(self):
#         self.fail('Make an employee test case')
#
#
# class RegistryOfStayTestCase(TestCase):
#
#     def setUp(self):
#         self.fail('Make an employee test case')
#
#     def test_passport_exists(self):
#         self.fail('create and check for existence of a passport')
#
#     def test_passport_expired(self):
#         self.fail('create several passports and an expired passport and check for expired passports')
#
#     def test_user_exists(self):
#         self.fail('Make an employee test case')
#
#
# class DocumentTestCase(TestCase):
#
#     def setUp(self):
#         self.fail('Make an employee test case')
#
#     def test_passport_exists(self):
#         self.fail('create and check for existence of a passport')
#
#     def test_passport_expired(self):
#         self.fail('create several passports and an expired passport and check for expired passports')
#
#     def test_user_exists(self):
#         self.fail('Make an employee test case')
#
#
# class EmployeeDocumentIntegrationTestCase(TestCase):
#
#     def setUp(self):
#         self.fail(
#             'Create an integration test where an employee is created,\
#              and then documents are added to their model')
#
