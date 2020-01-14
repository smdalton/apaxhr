# Generated by Django 3.0 on 2020-01-14 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(choices=[('N', 'APAX North'), ('S', 'APAX South')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('lc', 'Learning Center'), ('aw', 'Administrative Workplace'), ('ot', 'other')], max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.City')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Region')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Region'),
        ),
    ]
