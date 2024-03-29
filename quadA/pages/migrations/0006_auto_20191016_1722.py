# Generated by Django 2.2.6 on 2019-10-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20191016_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalHistoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('illness_cancer', models.BooleanField()),
                ('illness_aids', models.BooleanField()),
                ('illness_heart_disease', models.BooleanField()),
                ('illness_diabetes', models.BooleanField()),
                ('illness_asthma', models.BooleanField()),
                ('illness_renal_dialysis', models.BooleanField()),
                ('other_illness', models.CharField(max_length=200)),
                ('allergy_pollen', models.BooleanField()),
                ('allergy_dust', models.BooleanField()),
                ('allergy_nuts', models.BooleanField()),
                ('allergy_dairy', models.BooleanField()),
                ('allergy_wheat', models.BooleanField()),
                ('other_allergy', models.CharField(max_length=200)),
                ('medication', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='MedicalHistoryModels',
        ),
    ]
