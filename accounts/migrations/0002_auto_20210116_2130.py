# Generated by Django 3.1.5 on 2021-01-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='nip',
            field=models.CharField(default='199212052014121001', max_length=18),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nip_lama',
            field=models.CharField(default='340057019', max_length=9),
        ),
    ]
