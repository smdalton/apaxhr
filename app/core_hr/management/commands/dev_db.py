from django.core.management.base import BaseCommand, CommandError
from core_hr.models import User, Employee
from django.conf import settings
import os





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

    def create_user_employee(self, role, number):
        name = 'Test User#'+' '+str(number) + ' '+ role
        bio = 'This is a bio for Test User,  whose first name is Test and ' \
              'last name is User, who has email address testuser@abc.com, and lives on campus.'
        location = 'on'
        username = name.replace(' ', '')
        email = (username + '@abc.com').lower()
        user = User.objects.create_user(username=email, password='pass1234')
        user.is_superuser = False
        user.is_staff = False
        user.first_name = name.split(' ')[0]+str(number)
        user.last_name = name.split(' ')[1]
        user.email = email
        user.save()
        employee = Employee(user=user,middle_name='please update',bio=bio, employee_role='')
        employee.save()
        pass

    def create_super_user(self):
        bio = 'This is a bio for the admin user,  whose first name is admin and ' \
             'last name is istrator, who has no email address, and lives off campus.'

        user = User.objects.create_user('admin', password='pass1234')
        user.is_superuser = True
        user.is_staff = True
        user.first_name = 'Shane'
        user.last_name = 'Dalton'
        user.email = 'shanemdalton@gmail.com'
        user.save()
        employee = Employee(user=user, bio=bio, employee_role='sup')
        employee.save()
        pass

    def create_five_users(self):
        from core_hr.database_choices import roles

        for index in range(len(roles)):
            self.create_user_employee(role=roles[index][0], number=index)

    def collectstatic(self):
        os.system('python3 manage.py collectstatic --no-input')

    def run_server(self):
        os.system('python3 manage.py runserver 0.0.0.0:8000')

    def run_tests(self):
        # run simple test that checks to make sure the users were created and asuepruser exists

        pass

    def handle(self, **args):
        os.system('export DJANGO_COLORS="light;error=yellow/blue,blink;notice=magenta"')
        self.reset_db_and_migrations()
        self.create_five_users()
        self.create_super_user()
        self.collectstatic()
        #self.run_server()



