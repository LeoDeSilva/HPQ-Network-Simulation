# Generated by Django 4.0.1 on 2022-01-30 19:49

from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_request_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='body',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
        migrations.AlterField(
            model_name='request',
            name='header',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
        migrations.AlterField(
            model_name='request',
            name='server',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='server', to='Client.server'),
        ),
    ]
