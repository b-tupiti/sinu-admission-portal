# Generated by Django 4.1.6 on 2023-04-27 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_duration_length_course_duration_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='offered_mode',
        ),
        migrations.AddField(
            model_name='course',
            name='campus',
            field=models.CharField(choices=[('Kukum', 'Kukum'), ('Marine', 'Marine'), ('Panatina', 'Panatina')], default='Kukum', max_length=10, verbose_name='Offered Mode'),
        ),
        migrations.AlterField(
            model_name='course',
            name='qualification_level',
            field=models.CharField(choices=[('Degree', 'Degree'), ('Certificate', 'Certificate'), ('Diploma', 'Diploma'), ('Postgraduate Diploma', 'Postgraduate Diploma'), ('Masters', 'Masters')], default='Certificate', max_length=50),
        ),
    ]
