# Generated by Django 4.0.1 on 2022-01-30 20:53

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0005_server_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='header',
        ),
        migrations.AlterField(
            model_name='request',
            name='body',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
    ]
