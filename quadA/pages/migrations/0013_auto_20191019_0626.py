# Generated by Django 2.2.6 on 2019-10-19 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20191019_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescriptionmodel',
            old_name='images',
            new_name='image',
        ),
    ]
