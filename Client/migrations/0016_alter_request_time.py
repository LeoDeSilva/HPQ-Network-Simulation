# Generated by Django 4.0.1 on 2022-02-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0015_alter_request_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
