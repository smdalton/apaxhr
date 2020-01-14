from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
import core_hr.models as hr_models
from django.conf import settings
import os
from users.models import Employee
from faker import Faker
from core_hr.extras.core_hr_mock_factory import get_mock_passport, get_mock_user

fake=Faker()
Faker.seed(2323)
fake.phone_number()
fake.city()
fake.building_number()
fake.address()
fake.date_between(start_date="-30y", end_date="today")
fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115)
fake.day_of_month()
fake.month()
fake.year()
fake.bs()
fake.latlng()
fake.local_latlng(country_code="US", coords_only=False)
fake.local_latlng(country_code='VN', coords_only=True)
fake.date(pattern="%Y-%m-%d", end_datetime=None)

class Command(BaseCommand):
    help = "Initializes users, clears db, makes and applies migrations, runs server"

    def reset_db_and_migrations(self):
        self.stdout.write(os.getcwd())
        os.system('rm devdb.sqlite3')
        # safeguard for production database

        if settings.DATABASES['default']['NAME'].split('/')[-1] == "devdb.sqlite3":
            self.stdout.write('Deleting: '+ settings.DATABASES['default']['NAME'])
            os.system('find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
            os.system('find . -path "*/migrations/*.pyc"  -delete')
            os.system('python3 manage.py makemigrations --no-input')
            os.system('python3 manage.py migrate')
        else:
            self.stdout.write('Running on production postgresql wipe_db aborted')
            return

    def create_many_users(self):
        for x in range(25):
            get_mock_passport(get_mock_user())

    def create_super_user(self):
        print(os.getcwd())
        user = Employee.objects.create_superuser(email='smd@gmail.com',password='pass1234')
        user.save()


    def run_server(self):
        os.system('python3 manage.py runserver 0.0.0.0:8000')

    def run_tests(self):
        # run simple test that checks to make sure the users were created and asuepruser exists

        pass

    def handle(self, **args):
        os.system('export DJANGO_COLORS="light;error=yellow/blue,blink;notice=magenta"')
        self.reset_db_and_migrations()
        self.create_super_user()
        self.create_many_users()
        #self.run_server()



