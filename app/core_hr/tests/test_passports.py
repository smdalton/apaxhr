from django.test import TestCase
import faker
from core_hr.models import Passport
from users.models import Employee
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
import random
fake = faker.Faker()

def get_mock_user():
    User = Employee
    full_name = f"{fake.first_name()} {fake.last_name()} {fake.last_name()}"
    gender = random.choice([x[0] for x in Employee.genders])
    employee_id_code =f"G-{fake.ean8()}"

    employment_status = random.choice([x[0] for x in Employee.employment_statuses])
    employment_status_note = fake.bs()

    phone_number = fake.phone_number()
    email = fake.email()
    personal_email = fake.email()
    date_joined = fake.past_date(start_date="-120d", tzinfo=None)
    user = User.objects.create_user(
        full_name=full_name,
        gender=gender,
        employee_id_code=employee_id_code,
        employment_status=employment_status,
        employment_status_note= employment_status_note,
        phone_number=phone_number,
        personal_email=personal_email,
        date_joined=date_joined,
        email=email,
        password='foo'
    )

    return user

def get_mock_passport(employee):
    owner = Employee.objects.get(id=employee.id)
    dob = fake.date_between(start_date="-9y", end_date="-1m")
    date_of_expiration = fake.date_between(start_date="+3m", end_date="+9y")
    place_of_issue = fake.country_code()
    date_of_issue = fake.date_between(start_date="-9y", end_date="-1m")
    passport = Passport.objects.get_or_create(
        owner=owner,
        name=owner.full_name,
        place_of_issue=place_of_issue,
        issue_date=date_of_issue,
        expiration_date=date_of_expiration,
        dob=dob
    )
    return Passport

class PassportTestCase(TestCase):

    def test_passport_has_fields(self):
        mock_passport = get_mock_passport()
        retrieved_passport = Passport.objects.get_or_create(id=mock_passport.id)
        self.assertEqual(Passport.objects.get(mock_passport), retrieved_passport)
        self.fail('Make an employee test case')



    def test_passport_expiring_soon(self):
        self.fail('ensure the passport is not expiring within the next month')

    def test_passport_expired(self):
        self.fail('create several passports and an expired passport and check for expired passports')

    def test_user_exists(self):
        self.fail('Make an employee test case')

    # def test_employee_exists(self):
