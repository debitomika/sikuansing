# Generated by Django 3.1.5 on 2021-09-30 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_piaagregat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piaagregat',
            name='PIA',
            field=models.FloatField(default=0, null=True),
        ),
    ]
