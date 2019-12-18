from django.core.management.base import BaseCommand, CommandError
from employee_data.models import Employee, Passport, PublicImage, RegistryOfStayForm, User
import os





class Command(BaseCommand):
    help = "Initializes users, clears db, makes and applies migrations, runs server"

    def wipe_db(self):
        self.stdout.write(os.getcwd())
        pass

    def create_user_employee(self, role, number):
        name = 'Test User#'+' '+number + ' '+ role
        bio = 'This is a bio for Test User,  whose first name is Test and ' \
              'last name is User, who has email address testuser@abc.com, and lives on campus.'
        location = 'on'
        username = name.replace(' ', '')
        email = (username + '@abc.com').lower()
        user = User.objects.create_user(username=email, password='pass1234')
        user.is_superuser = False
        user.is_staff = False
        user.first_name = name.split(' ')[0]
        user.last_name = name.split(' ')[1]
        user.email = email
        user.save()
        employee = Employee(user=user,middle_name='please update',biography=bio, employee_role='')
        employee.save()
        pass

    def create_super_user(self):
        pass

    def create_five_users(self):
        pass



    def handle(self, **args):
        os.system('export DJANGO_COLORS="light;error=yellow/blue,blink;notice=magenta"')
        self.wipe_db()


