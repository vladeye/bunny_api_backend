# Generated by Django 2.0.1 on 2018-01-31 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_readings_reads'),
    ]

    operations = [
        migrations.AddField(
            model_name='readings',
            name='status_api',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='readings',
            name='status_reads',
            field=models.CharField(default='N', max_length=1),
        ),
    ]
