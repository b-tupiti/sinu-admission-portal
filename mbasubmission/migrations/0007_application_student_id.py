# Generated by Django 4.1.6 on 2023-03-16 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbasubmission', '0006_alter_application_application_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='student_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
