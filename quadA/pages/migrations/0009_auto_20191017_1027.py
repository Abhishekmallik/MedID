# Generated by Django 2.2.6 on 2019-10-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_signupmedicalinsurancemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmedicalinsurancemodel',
            name='occupation',
            field=models.CharField(max_length=18),
        ),
    ]
