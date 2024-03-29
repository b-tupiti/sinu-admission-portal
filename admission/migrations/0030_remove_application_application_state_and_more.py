# Generated by Django 4.1.6 on 2023-10-27 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0029_application_deposit_slip_application_letter_of_offer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='application_state',
        ),
        migrations.AddField(
            model_name='application',
            name='application_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('pending_deposit_verification', 'Pending Deposit Verification'), ('under_assessment', 'Under Assessment'), ('approved_and_offer_granted', 'Approved and Offer Granted')], default='draft', max_length=40, verbose_name='State of Application'),
        ),
    ]
