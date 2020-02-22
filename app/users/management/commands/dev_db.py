import time
import os
import random

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from users.models import Employee

from core_hr.extras.core_hr_mock_factory import \
    create_mock_user, create_mock_work_permit, create_mock_passport,\
    create_mock_ros_form, create_mock_teaching_certificate,\
    create_mock_achievement_certificate, \
    create_mock_degree, create_mock_resume

#
# fake=Faker()
# Faker.seed(2323)
# fake.phone_number()
# fake.city()
# fake.building_number()
# fake.address()
# fake.date_between(start_date="-30y", end_date="today")
# fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115)
# fake.day_of_month()
# fake.month()
# fake.year()
# fake.bs()
# fake.latlng()
# fake.local_latlng(country_code="US", coords_only=False)
# fake.local_latlng(country_code='VN', coords_only=True)
# fake.date(pattern="%Y-%m-%d", end_datetime=None)

class Command(BaseCommand):
    help = "Initializes users, clears db, makes and applies migrations, runs server"

    def reset_db_and_migrations(self):
        self.stdout.write(os.getcwd())
        # print("deleting db")
        # os.system('rm devdb.sqlite3')
        # time.sleep(1)
        # os.system('touch devdb.sqlite3')
        # os.system('chmod 777 devdb.sqlite3')
        # safeguard for production database

        if os.environ.get("DEV_POSTGRES")=='TRUE':

            self.stdout.write('Running dev postgres')
            print('deleting migrations')
            os.system('find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
            os.system('find . -path "*/migrations/*.pyc"  -delete')
            print('done')
            print("Waiting for db")
            os.system('python3 manage.py makemigrations --no-input')
            os.system('python3 manage.py migrate')

        else:
            self.stdout.write('Running on development postgresql wipe_db aborted')
            return

    def create_many_users_and_documents(self, num_users=15):
        for x in range(num_users):
            user = create_mock_user()
            if x % 5 == 0:print(x)
            create_mock_passport(
                user,
                has_image=random.choice([True, True, False]),
                expired=random.choice([False, False,True])
            )
            create_mock_ros_form(
                user,
                has_image=random.choice([True, True, False]),
                expired=random.choice([True, False, False, False])
            )
            create_mock_work_permit(
                user,
                has_image=random.choice([True, True, False]),
                expired=random.choice([True, False, False, False])
            )
            create_mock_achievement_certificate(user)
            create_mock_degree(user)
            create_mock_teaching_certificate(user)
            create_mock_resume(user)

    def create_super_user(self):
        user = Employee.objects.create_superuser(email='smd@gmail.com',password='pass1234')
        #user.save()

    def load_admin_themes(self):
        themes =  [
            'admin_interface_theme_foundation.json',
            'admin_interface_theme_django.json',
            'admin_interface_theme_bootstrap.json',
            'admin_interface_theme_uswds.json',
                      ]
        for theme in themes:
            call_command('loaddata', theme)



    def run_server(self):
        os.system('python3 manage.py runserver 0.0.0.0:8000')

    def run_tests(self):
        # run simple test that checks to make sure the users were created and asuepruser exists

        pass

    def handle(self, **args):
        os.system('export DJANGO_COLORS="light;error=yellow/blue,blink;notice=magenta"')
        import time
        self.reset_db_and_migrations()
        self.create_super_user()
        self.create_many_users_and_documents(num_users=5)
        self.load_admin_themes()
