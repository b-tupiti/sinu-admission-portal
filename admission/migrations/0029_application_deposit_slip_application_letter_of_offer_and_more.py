# Generated by Django 4.1.6 on 2023-10-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0028_alter_employment_month_year_ended_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='deposit_slip',
            field=models.FileField(blank=True, null=True, upload_to='slips/', verbose_name='Deposit Slip'),
        ),
        migrations.AddField(
            model_name='application',
            name='letter_of_offer',
            field=models.FileField(blank=True, null=True, upload_to='offer_letters/', verbose_name='Letter of Offer'),
        ),
        migrations.AddField(
            model_name='application',
            name='receipt',
            field=models.FileField(blank=True, null=True, upload_to='receipts/', verbose_name='Receipt'),
        ),
    ]
