# Generated by Django 3.1.5 on 2021-07-28 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_foto_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='foto_profil',
            field=models.ImageField(default='default.jpg', upload_to='foto_profil'),
        ),
    ]
