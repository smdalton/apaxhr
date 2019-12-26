# Generated by Django 3.0 on 2019-12-18 07:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=25)),
                ('middle_name', models.CharField(default='', max_length=25)),
                ('last_name', models.CharField(default='', max_length=25)),
                ('bio', models.TextField(default='', max_length=1000)),
                ('employee_role', models.CharField(choices=[('ftt', 'Full Time Teacher'), ('pt', 'Part Time Teacher'), ('training', 'Teacher in Training'), ('ht', 'Head Teacher'), ('st', 'Senior Teacher'), ('sup', 'Support Staff')], default='', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkPermit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration', models.DateTimeField(default=datetime.datetime(2019, 12, 18, 7, 30, 51, 222395))),
                ('pdf', models.FileField(null=True, upload_to='document_images')),
                ('image', models.ImageField(blank=True, null=True, upload_to='work_permit_images')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee_data.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='RegistryOfStayForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration', models.DateTimeField(default=datetime.datetime(2019, 12, 18, 7, 30, 51, 222395))),
                ('issued', models.DateTimeField(default=datetime.datetime(2019, 12, 18, 7, 30, 51, 222395))),
                ('pdf', models.FileField(null=True, upload_to='document_images')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee_data.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='PublicImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', max_length=25)),
                ('image', models.ImageField(null=True, upload_to='profile_pictures')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_data.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_date', models.DateTimeField(default=datetime.datetime(2019, 12, 18, 7, 30, 51, 222395))),
                ('issue_date', models.DateTimeField(default=datetime.datetime(2019, 12, 18, 7, 30, 51, 222395))),
                ('image', models.ImageField(upload_to='')),
                ('pdf', models.FileField(upload_to='')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee_data.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeWorkHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_data.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='document_images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_data.Employee')),
            ],
        ),
    ]
