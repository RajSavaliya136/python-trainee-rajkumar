# Generated by Django 5.0.3 on 2024-03-28 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_alter_doctorregistration_last_login_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorregistration',
            name='adhar_no',
        ),
        migrations.RemoveField(
            model_name='doctorregistration',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='doctorregistration',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='doctorregistration',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='doctorregistration',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='doctorregistration',
            name='role',
        ),
        migrations.RemoveField(
            model_name='patientregistration',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='patientregistration',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='patientregistration',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='patientregistration',
            name='next_appointment',
        ),
        migrations.RemoveField(
            model_name='patientregistration',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='patientregistration',
            name='suggetion',
        ),
    ]
