# Generated by Django 3.0 on 2020-03-11 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BiWeeklyClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.SmallIntegerField(choices=[(1, 'Block 1 8:00 - 9:30'), (2, 'Block 2 9:30 - 11:15 '), (3, 'Block 3 14:00 - 15:30'), (4, 'Block 4 15:45 - 17:15'), (5, 'Block 5 17:30 - 19:00'), (6, 'Block 6 19:15 - 20:45')])),
                ('other_note', models.TextField(default='not an other course', max_length=85, verbose_name='Fill out this note if you have selected an other type class')),
                ('recurring', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('day1', models.SmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday'), (8, 'Sunday Am'), (9, 'Unused')], default=9)),
                ('day2', models.SmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday'), (8, 'Sunday Am'), (9, 'Unused')], default=9)),
                ('single_day', models.BooleanField(default=False)),
                ('class_title', models.CharField(max_length=25)),
                ('cm', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CenterDailySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=-1)),
                ('weekday', models.PositiveSmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday'), (8, 'Sunday Am'), (9, 'Unused')], default=8)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CenterRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=-1, max_length=12, verbose_name="If these aren't named exactly and consistently room checking will not work")),
                ('note', models.TextField(max_length=250, verbose_name='Note any important details about a room here')),
            ],
        ),
        migrations.CreateModel(
            name='LearningCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('name', models.CharField(max_length=40, unique=True)),
                ('city', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledClass',
            fields=[
                ('biweeklyclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='centers.BiWeeklyClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('centers.biweeklyclass', models.Model),
        ),
        migrations.CreateModel(
            name='CenterWeeklySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_start', models.DateField(auto_now_add=True)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='centers.LearningCenter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CenterTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('preferred_room', models.SmallIntegerField(default=-1)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centers.LearningCenter')),
            ],
        ),
    ]
