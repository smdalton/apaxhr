# Generated by Django 3.0 on 2020-03-27 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='salariedposition',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salariedposition',
            name='employment_contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employment.EmploymentContract'),
        ),
    ]
