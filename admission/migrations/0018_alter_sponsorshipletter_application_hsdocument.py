# Generated by Django 4.1.6 on 2023-07-20 02:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0017_sponsorshipletter_delete_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorshipletter',
            name='application',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor_letter', to='admission.application'),
        ),
        migrations.CreateModel(
            name='HSDocument',
            fields=[
                ('file', models.FileField(upload_to='documents/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('form_level', models.CharField(choices=[('form_3', 'Form 3'), ('form_5', 'Form 5'), ('form_6', 'Form 6'), ('foundation', 'Foundation or (Form 7)')], max_length=20, verbose_name='Form Level')),
                ('document_type', models.CharField(choices=[('transcript', 'Acadmic Transcript'), ('certificate', 'Academic Certificate')], max_length=20, verbose_name='Document Type')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='high_school_document', to='admission.application')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
