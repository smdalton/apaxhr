# Generated by Django 3.0 on 2020-02-11 07:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('full_name', models.CharField(max_length=45, validators=[django.core.validators.RegexValidator('^[a-z A-Z]*$', 'Only Alphabetic characters allowed')], verbose_name='Name as on Passport')),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=1)),
                ('employee_id_number', models.CharField(max_length=20, null=True, verbose_name='employee id number')),
                ('employment_status', models.CharField(choices=[('ap', 'Applicant'), ('trial', 'Initial Training'), ('em', 'Employed'), ('ps', 'Pause')], max_length=30)),
                ('employment_status_note', models.TextField(max_length=500)),
                ('phone_number', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='APAX email address')),
                ('personal_email', models.EmailField(max_length=254, unique=True, verbose_name='Personal Email Address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='profile_images', verbose_name='Upload Profile Image')),
                ('bio', models.TextField(blank=True, max_length=500, null=True, verbose_name='Personal Biography')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_applicant', models.BooleanField(default=True)),
                ('is_trainee', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_head_teacher', models.BooleanField(default=False)),
                ('is_faculty_manager', models.BooleanField(default=False)),
                ('is_area_manager', models.BooleanField(default=False)),
                ('is_hr_manager', models.BooleanField(default=False)),
                ('is_hr_director', models.BooleanField(default=False)),
                ('is_teacher_management_director', models.BooleanField(default=False)),
                ('is_training_director', models.BooleanField(default=False)),
                ('is_recruiting_director', models.BooleanField(default=False)),
                ('is_head_office', models.BooleanField(default=False)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
