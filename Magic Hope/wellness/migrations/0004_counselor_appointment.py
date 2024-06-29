# Generated by Django 5.0.6 on 2024-06-29 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellness', '0003_course_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counselor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('counselor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wellness.counselor')),
            ],
        ),
    ]
