from django.contrib.auth.models import User
from django.forms import SplitDateTimeField
from django.test import TestCase
from .models import Passport, Employee
from. import views
import datetime
from django.utils import timezone
# Create your tests here.


class EmployeeTestCase(TestCase):
    pass


class PassportTestCase(TestCase):

    def setUp(self):
        self.date = datetime.datetime.now()
        self.user = User.objects.create_user(username="admin")
        self.employee = Employee.objects.create(user=self.user, date_joined=self.date)
        self.passport = Passport.objects.create(owner=self.employee, expiration=self.date)

    def test_passport_exists(self):
        passport = Passport.objects.get(owner__user__username="admin")
        self.assertEqual(passport, self.passport, 'passports do not match')

    def test_user_exists(self):
        user = User.objects.get(employee_user=self.employee)
        self.assertEquals(user, self.user, 'users do not match')
    # def test_employee_exists(self):


class DataBaseConnectionTestCase(TestCase):
    pass