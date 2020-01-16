from django.test import TestCase
import faker
from core_hr.models import Passport
from users.models import Employee
from django.core.files.uploadedfile import SimpleUploadedFile
import django_countries
import os
#http://giflib.sourceforge.net/whatsinagif/bits_and_bytes.html


fake = faker.Faker()

from core_hr.extras.core_hr_mock_factory import get_mock_user, get_mock_photo


def get_mock_passport(employee,expired=False,has_image=True):

    dob=fake.date_between(start_date="-49y", end_date="-21y")
    date_of_expiration = fake.date_between(start_date="-6m", end_date="+9y")
    place_of_issue = fake.country_code()
    date_of_issue = fake.date_between(start_date="-9y", end_date="-1m")
    if expired:
        date_of_expiration = fake.date_between(start_date="-1y", end_date='-1m')
    if has_image:
        photo = get_mock_photo()
    else:
        photo = None

    owner= Employee.objects.get(pk=employee.pk)
    passport = Passport.objects.create(
        owner=owner,
        place_of_issue=place_of_issue,
        issue_date=date_of_issue,
        expiration_date=date_of_expiration,
        dob=dob,
        image=photo
    )

    return passport




class PassportTestCase(TestCase):

    def setUp(self):
        self.employee = get_mock_user()
        self.passport = get_mock_passport(self.employee)

    def test_passport_saves_and_retrieves(self):
        retrieved_passport = Passport.objects.get(id=self.passport.pk)
        self.assertEqual(self.passport, retrieved_passport)

    def test_passport_is_not_expired(self):
        valid_passport = get_mock_passport(get_mock_user(), has_image=False)
        self.assertEqual(valid_passport.expired, False)

    def test_passport_is_expired(self):
        expired_passport = get_mock_passport(get_mock_user(),expired=True)
        self.assertEqual(expired_passport.expired, True)

    def test_passport_data_complete(self):
        complete_passport = get_mock_passport(get_mock_user())
        self.assertEqual(complete_passport.data_complete, True)

    def test_passport_data_not_complete(self):
        incomplete_passport = get_mock_passport(get_mock_user(), has_image=False)
        self.assertEqual(incomplete_passport.data_complete, False)



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
