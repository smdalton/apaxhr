# Generated by Django 3.0 on 2020-01-10 07:55

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core_hr', '0002_auto_20200110_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='passport',
            name='place_of_issue',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]
