# Generated by Django 4.1.6 on 2023-07-24 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0019_alter_hsdocument_application'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ApplicationToken',
        ),
    ]
