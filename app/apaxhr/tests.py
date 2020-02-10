from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.urls import resolve
from . import views


class ApaxHomePageTestCase(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func.view_class, views.HomePageView)

