from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


class Employee(AbstractBaseUser, PermissionsMixin):
    # first_name = models.CharField(_('first name'), max_length=25, blank=False, null=True)
    # middle_name = models.CharField(_('Middle Name'), max_length=25, blank=False, null=True)
    # last_name = models.CharField(_('Last Name'), max_length=25, blank=False, null=True)
    # bio = models.TextField(_('Personal Biography'), max_length=500, blank=True, null=True)

    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
