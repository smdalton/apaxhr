from django.test import TestCase
import faker
from core_hr.models import Passport
from users.models import Employee
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
import random
fake = faker.Faker()
from .mock_factory import get_mock_user, get_mock_passport


class PassportTestCase(TestCase):

    def setUp(self):
        self.employee = get_mock_user()
        self.passport = get_mock_passport(self.employee)

    def test_passport_saves_and_retrieves(self):
        retrieved_passport = Passport.objects.get(id=self.passport.pk)
        self.assertEqual(self.passport, retrieved_passport)

    #
    #
    # def test_passport_expiring_soon(self):
    #     self.fail('ensure the passport is not expiring within the next month')
    #
    # def test_passport_expired(self):
    #     self.fail('create several passports and an expired passport and check for expired passports')
    #
    # def test_user_exists(self):
    #     self.fail('Make an employee test case')

    # def test_employee_exists(self):
