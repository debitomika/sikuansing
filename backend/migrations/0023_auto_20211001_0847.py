# Generated by Django 3.1.5 on 2021-10-01 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_auto_20210930_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterkegiatan',
            name='satuan',
            field=models.CharField(max_length=60),
        ),
    ]
