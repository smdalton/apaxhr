from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
import core_hr.models as hr_models
from django.conf import settings
import os
from users.models import Employee
from faker import Faker
from . import fake_helper

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

    # def create_user_employee(self, role, number):
    #     name = 'Test User#'+' '+str(number) + ' '+ role
    #     bio = 'This is a bio for a Test User,  whose first name is Test and ' \
    #           'last name is User, who has email address testuser@abc.com'
    #     location = 'on'
    #     username = name.replace(' ', '')
    #     email = (username + '@abc.com').lower()
    #     user = Employee.objects.create_user(email=email, password='pass1234')
    #     user.is_superuser = False
    #     user.is_staff = False
    #     user.first_name = name.split(' ')[0]+str(number)
    #     user.last_name = name.split(' ')[1]
    #     user.email = email
    #     user.save()
    #     employee = hr_models.Employee(user=user, middle_name='please update', bio=bio, employee_role='')
    #     employee.save()
    #     pass

    def create_super_user(self):
        print(os.getcwd())
        user = Employee.objects.create_superuser(email='smd@gmail.com',password='pass1234')
        user.save()
        #
        # bio = 'This is a bio for the admin user,  whose first name is admin and ' \
        #      'last name is istrator, who has no email address, and lives off campus.'
        #
        # user = Employee.objects.create_superuser('admin', password='pass1234')
        # user.first_name = 'Shane'
        # user.last_name = 'Dalton'
        # user.email = 'shanemdalton@gmail.com'
        # user.save()
        # employee = hr_models.Employee(user=user, bio=bio, employee_role='sup')
        # employee.save()
        # pass

    def create_five_users(self):
        for i in len(range(6)):
            Employee.objects.get_or_create(email=fake.email(),password='pass1234')



    def run_server(self):
        os.system('python3 manage.py runserver 0.0.0.0:8000')

    def run_tests(self):
        # run simple test that checks to make sure the users were created and asuepruser exists

        pass

    def handle(self, **args):
        os.system('export DJANGO_COLORS="light;error=yellow/blue,blink;notice=magenta"')
        self.reset_db_and_migrations()
        #self.create_five_users()
        self.create_super_user()
        #self.run_server()



