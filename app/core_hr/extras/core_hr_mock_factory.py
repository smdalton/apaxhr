from datetime import datetime, timedelta

from django.db.models import ImageField
from django.test import TestCase
import faker
from core_hr.models import Passport, RegistryOfStayForm
from users.models import Employee
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
import random
import mock
from django.core.files.uploadedfile import SimpleUploadedFile
import os

fake = faker.Faker()




def get_mock_user():
    User = Employee
    full_name = f"{fake.first_name()} {fake.last_name()} {fake.last_name()}"
    gender = random.choice([x[0] for x in Employee.genders])
    employee_id_number = f"G-{fake.ean8()}"
    employment_status = random.choice(
        [x[0] for x in Employee.employment_statuses])
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


def get_mock_ros_form(employee):

    employee_address = fake.address()
    landlords_name = fake.name()
    landlords_cell_phone = fake.phone_number()
    landlords_email = fake.email()
    issued = fake.date_between(start_date="-15d", end_date="-1d")
    expiration=datetime.now().date() + timedelta(days=180)
    image = None

    form = RegistryOfStayForm.objects.create(
        employee=employee,
        employee_address=employee_address,
        landlords_name=landlords_name,
        landlords_cell_phone=landlords_cell_phone,
        landlords_email=landlords_email,
        issued = issued,
        expiration=expiration,
        image=image

    )
    return form

def get_mock_work_permit(employee):
    pass

def get_mock_resume(employee):
    pass


def get_mock_achievement_certificate(employee):
    pass


def get_mock_tefl_form(employee):
    pass


def get_mock_degree(employee):
    pass
