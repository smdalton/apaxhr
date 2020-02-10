# Generated by Django 3.0 on 2020-02-10 05:58

import apaxhr.storage_backends
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ImageField(storage=apaxhr.storage_backends.PrivateMediaStorage(), upload_to='kpi_certificates')),
                ('message_text', models.TextField(max_length=1000, verbose_name='Enter award message for email here')),
            ],
            options={
                'verbose_name': '\u200bFAS/KPI Certificate',
            },
        ),
        migrations.CreateModel(
            name='DegreeDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ImageField(storage=apaxhr.storage_backends.PrivateMediaStorage(), upload_to='degree_certs')),
            ],
            options={
                'verbose_name': '\u200bDegree Document',
            },
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('issue_date', models.DateField(verbose_name='Document Date of Issue')),
                ('expiration_date', models.DateField(verbose_name='Document Expiration Date')),
                ('dob', models.DateField()),
                ('place_of_issue', django_countries.fields.CountryField(default='AQ', max_length=2)),
                ('image', models.ImageField(storage=apaxhr.storage_backends.PrivateMediaStorage(), upload_to='passports')),
            ],
            options={
                'verbose_name': 'Passport',
            },
        ),
        migrations.CreateModel(
            name='RegistryOfStay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('issue_date', models.DateField(verbose_name='Document Date of Issue')),
                ('expiration_date', models.DateField(verbose_name='Document Expiration Date')),
                ('employee_address', models.CharField(max_length=100)),
                ('landlords_name', models.CharField(max_length=100)),
                ('landlords_cell_phone', models.CharField(max_length=25)),
                ('landlords_email', models.EmailField(max_length=40)),
                ('image', models.ImageField(storage=apaxhr.storage_backends.PrivateMediaStorage(), upload_to='ros_images')),
            ],
            options={
                'verbose_name': 'Registry of Stay Form',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('rs', 'Resume'), ('cv', 'Curriculum Vitae')], max_length=20)),
                ('image', models.ImageField(storage=apaxhr.storage_backends.PrivateMediaStorage(), upload_to='resumes_cvs')),
            ],
            options={
                'verbose_name': "\u200bResume and CV'",
            },
        ),
        migrations.CreateModel(
            name='TeachingCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('id_number', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('c', 'CELTA'), ('ts', 'TESOL'), ('tf', 'TEFL'), ('ot', 'other')], max_length=15)),
                ('image', models.ImageField(storage=apaxhr.storage_backends.PrivateMediaStorage(), upload_to='tefl_certs')),
            ],
            options={
                'verbose_name': '\u200bTESL/TESOL/CELTA/TEFL etc. certifcates',
            },
        ),
        migrations.CreateModel(
            name='WorkPermit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('issue_date', models.DateField(verbose_name='Document Date of Issue')),
                ('expiration_date', models.DateField(verbose_name='Document Expiration Date')),
                ('image', models.ImageField(storage=apaxhr.storage_backends.PrivateMediaStorage(), upload_to='default_images')),
                ('type', models.CharField(choices=[('wp', 'Work Permit'), ('vs', 'visa')], max_length=2)),
            ],
            options={
                'verbose_name': 'Work Permit and Visa',
            },
        ),
    ]
