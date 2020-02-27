from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from core_hr.tasks import core_hr_task
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apaxhr.settings')

app = Celery('app')

app.config_from_object('django.conf:settings', namespace='CELERY')

# load tasks from each django app config in settings
# lambda: settings.INSTALLED_APPS
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
@app.task(bind=True)
def debug_task(self):
    print('Request{0!r}'.format(self.request))

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(100.0, test('hello'), name='add every 5')
    sender.add_periodic_task(4.0, core_hr_task(), name='module test' )


@app.task
def test(arg):
    print(arg)