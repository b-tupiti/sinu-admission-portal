# Generated by Django 4.1.6 on 2023-02-28 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='name',
        ),
    ]
