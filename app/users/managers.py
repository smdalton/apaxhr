from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _



"""
https://testdriven.io/blog/django-custom-user-model/
"""

class CustomUserManager(BaseUserManager):
    """
    Custom User model with email as unique identifier
    for authentication
    instead of default username
    """

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    def employees_with_passports(self):

        from core_hr.models import Passport
        from users.models import Employee
        # Todo: Expand this method into the django admin filter bars for completeness
        # Employee.objects.filter(pk__in=Subquery(Passport.objects.all().values('owner__pk')))
        passports = Passport.objects.values_list('owner__pk',flat=True).count()
        not_passports = Employee.objects.count() - passports
        return passports



    # from core_hr.models import Passport, RegistryOfStay, WorkPermit
    # ros_forms = RegistryOfStay.objects.all()
    # work_permit = WorkPermit.objects.all()
    # passport_id_set = passports.distinct()
