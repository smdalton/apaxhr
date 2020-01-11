from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.urls import resolve
from core_hr import views



class SmokeTest(TestCase):
    def test_math(self):
        self.assertEqual((1+1),2)

class ApaxHomePageTestCase(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func.view_class, views.ApaxHomePageView)

