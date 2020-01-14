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
    employee_id_number =f"G-{fake.ean8()}"

    employment_status = random.choice([x[0] for x in Employee.employment_statuses])
    employment_status_note = fake.bs()

    phone_number = fake.phone_number()
    email = fake.email()
    personal_email = fake.email()

    date_joined = fake.past_date(start_date="-120d", tzinfo=None)

    user = User.objects.create_user(
        full_name=full_name,
        gender=gender,
        employee_id_number=employee_id_number,
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
    owner = Employee.objects.get(pk=employee.pk)
    dob = fake.date_between(start_date="-9y", end_date="-1m")
    date_of_expiration = fake.date_between(start_date="+3m", end_date="+9y")
    place_of_issue = fake.country_code()
    date_of_issue = fake.date_between(start_date="-9y", end_date="-1m")


    passport = Passport.objects.create(
        owner=owner,
        place_of_issue=place_of_issue,
        issue_date=date_of_issue,
        expiration_date=date_of_expiration,
        dob=dob
    )
    return passport
