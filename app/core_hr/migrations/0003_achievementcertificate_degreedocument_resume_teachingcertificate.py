# Generated by Django 3.0 on 2020-01-16 05:20

import apaxhr.storage_backends
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core_hr', '0002_auto_20200116_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachingCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, choices=[('c', 'CELTA'), ('ts', 'TESOL'), ('tf', 'TEFL'), ('ot', 'other')], max_length=15, null=True)),
                ('image', models.ImageField(storage=apaxhr.storage_backends.PrivateMediaStorage(), upload_to='tefl_certs')),
                ('added', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('rs', 'Resume'), ('cv', 'Curriculum Vitae')], max_length=20)),
                ('image', models.ImageField(blank=True, null=True, storage=apaxhr.storage_backends.PrivateMediaStorage(), upload_to='resumes')),
                ('added', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DegreeDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AchievementCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(storage=apaxhr.storage_backends.PrivateMediaStorage(), upload_to='kpi_certificates')),
                ('message_text', models.TextField(max_length=1000, verbose_name='Enter award message for email here')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
