# Generated by Django 4.1.6 on 2023-06-20 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0014_application_current_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='current_section',
            field=models.CharField(choices=[('personal_details', 'Personal Details'), ('sponsor_details', 'Sponsor Details'), ('education_background', 'Education Background'), ('employment_history', 'Employment History'), ('declaration', 'Declaration')], default='personal_details', max_length=40, verbose_name='Current Section (keeps track of the section currently on edit)'),
        ),
    ]