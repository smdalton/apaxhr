from __future__ import absolute_import, unicode_literals

from celery import shared_task


from users.models import Employee


@shared_task
def add(x, y):
    return x + y

@shared_task
def hello():
    return 'Hello'

@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_employees():
    return Employee.objects.count()
