# Generated by Django 4.1.6 on 2023-07-24 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0020_delete_applicationtoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='course',
        ),
        migrations.RemoveField(
            model_name='application',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='application',
            name='major',
        ),
        migrations.RemoveField(
            model_name='application',
            name='year_end',
        ),
        migrations.RemoveField(
            model_name='application',
            name='year_start',
        ),
    ]
