from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission
from users.models import Employee


class Command(BaseCommand):

    def __init__(self):

        self.groups = [
            'Applicants',
            'Trainees',
            'Teachers',



            'Head Teachers',
            'Faculty Managers',
            'Area Managers',
            'HR Managers',

            'Teacher Management Directors',
            'Training Directors',
            'Recruiting Directors',

            'HR Directors',
            'Developers'
        ]
        self.tier1 = [
            'Applicants',
            'Trainees',
            'Teachers',
        ]
        self.tier2 = [
            'Head Teachers',
            'Faculty Managers',

        ]
        self.tier3 = [
            # documents and PII
            'Area Managers',
            'HR Managers',
        ]
        self.tier4 = [
            # No documents and PII
            'Teacher Management Directors',
            'Training Directors',
            'Recruiting Directors',
        ]
        self.tier5 = [
            'HR Directors',
            'Developers'
        ]
    def create_groups(self):
        for group_name in self.groups:
            obj, created = Group.objects.get_or_create(name=group_name)


    def make_all_tiers_employee(self):
        tier1 = Employee.objects.create(
            email='tier1@gmail.com',
            password='pass1234',
        )
        # applicants
        teachers = Group.objects.get(name='Teachers')
        teachers.user_set.add(tier1)

        tier2 = Employee.objects.create(
            email='tier2@gmail.com',
            password='pass1234'
        )
        fms = Group.objects.get(name='Faculty Managers')
        fms.user_set.add(tier2)

        tier3 = Employee.objects.create(
            email='tier3@gmail.com',
            password='pass1234'
        )
        ams = Group.objects.get(name='Area Managers')
        ams.user_set.add(tier3)

        tier4 = Employee.objects.create(
            email='tier4@gmail.com',
            password='pass1234'
        )
        directors = Group.objects.get(name='Area Managers')
        directors.user_set.add(tier4)



    def assign_tier1_permissions(self, user_list):

        permissions = []
        # document creation, document viewing, no admin access


        for group_name in self.tier1:
            group = Group.objects.get(name=group_name)
            group.permissions = permissions

            pass
        # document creation
    def assign_tier2_permissions(self, user_list):

        """"""
        permissions = []
        for group_name in self.tier2:
            group = Group.objects.get(name=group_name)
            group.permissions = permissions

            pass

    def assign_tier3_permissions(self, user_list):
        permissions = []

        for group_name in self.tier3:
            group = Group.objects.get(name=group_name)
            group.permissions = permissions

            pass


    def assign_tier4_permissions(self):
        permissions = []

        for group_name in self.tier4:
            group = Group.objects.get(name=group_name)
            group.permissions = permissions

            pass


    def assign_permissions(self):
        pass


    def create_permission_users(self):
        pass



    def handle(self, *args, **options):
        print('Setting permissions')
        self.create_groups()
        self.make_all_tiers_employee()
