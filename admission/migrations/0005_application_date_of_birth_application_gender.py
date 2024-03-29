# Generated by Django 4.1.6 on 2023-03-06 04:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0004_alter_application_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='male', max_length=6),
            preserve_default=False,
        ),
    ]
