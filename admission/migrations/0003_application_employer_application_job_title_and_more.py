# Generated by Django 4.1.6 on 2023-03-06 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0002_remove_document_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='employer',
            field=models.CharField(default='nil', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='job_title',
            field=models.CharField(default='nil', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='title',
            field=models.CharField(choices=[('MR', 'MR'), ('MRS', 'MRS'), ('MS', 'MS'), ('DR', 'DR')], default='MRS', max_length=3),
            preserve_default=False,
        ),
    ]