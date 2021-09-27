# Generated by Django 3.1.5 on 2021-07-07 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210128_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='jabatan_kantor',
            field=models.CharField(choices=[('1', 'Kepala BPS'), ('2', 'Kepala Subbagian Umum'), ('3', 'Koordinator Fungsi Statistik Sosial'), ('4', 'Koordinator Fungsi Statistik Produksi'), ('5', 'Koordinator Fungsi Statistik Distribusi'), ('6', 'Koordinator Fungsi Neraca Wilayah dan Analisis Statistik'), ('7', 'Koordinator Fungsi Integrasi Pengolahan dan Diseminasi Statistik'), ('8', 'Staf Subbagian Umum'), ('9', 'Staf Subbagian Umum'), ('10', 'Staf Subbagian Umum'), ('11', 'Staf Subbagian Umum'), ('12', 'Staf Subbagian Umum'), ('13', 'Staf Subbagian Umum'), ('14', 'KSK Kuantan Mudik'), ('15', 'KSK Hulu Kuantan'), ('16', 'KSK Gunung Toar'), ('17', 'KSK Pucuk Rantau'), ('18', 'KSK Singingi'), ('19', 'KSK Singingi Hilir'), ('20', 'KSK Kuantan Tengah'), ('21', 'KSK Sentajo Raya'), ('22', 'KSK Benai'), ('23', 'KSK Kuantan Hilir'), ('24', 'KSK Pangean'), ('25', 'KSK Logas Tanah Darat'), ('26', 'KSK Kuantan Hilir Seberang'), ('27', 'KSK Cerenti'), ('28', 'KSK Inuman')], default='7', max_length=80),
        ),
    ]
