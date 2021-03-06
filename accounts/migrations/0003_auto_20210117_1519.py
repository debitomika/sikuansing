# Generated by Django 3.1.5 on 2021-01-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210116_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='jabatan_fungsional',
            field=models.CharField(choices=[('0', 'Fungsional Umum'), ('1', 'Statistisi Pelaksana'), ('2', 'Statistisi Pelaksana Lanjutan'), ('3', 'Statistisi Penyelia'), ('4', 'Statistisi Pertama'), ('5', 'Statistisi Muda'), ('6', 'Statistisi Madya'), ('7', 'Statistisi Utama'), ('8', 'Pranata Komputer Terampil'), ('9', 'Pranata Komputer Mahir'), ('10', 'Pranata Komputer Penyelia'), ('11', 'Pranata Komputer Ahli Pertama'), ('12', 'Pranata Komputer Ahli Muda'), ('13', 'Pranata Komputer Ahli Madya'), ('14', 'Pranata Komputer Ahli Utama')], default='12', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='jabatan_kantor',
            field=models.CharField(choices=[('1', 'Kepala BPS'), ('2', 'Kepala Subbagian Umum'), ('3', 'Koordinator Fungsi Statistik Sosial'), ('4', 'Koordinator Fungsi Statistik Produksi'), ('5', 'Koordinator Fungsi Statistik Distribusi'), ('6', 'Koordinator Fungsi Neraca Wilayah dan Analisis Statistik'), ('7', 'Koordinator Fungsi Integrasi Pengolahan dan Diseminasi Statistik'), ('8', 'Staf'), ('9', 'KSK')], default='7', max_length=80),
        ),
        migrations.AddField(
            model_name='customuser',
            name='no_hp',
            field=models.CharField(default='081316658226', max_length=14),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pangkat_golongan',
            field=models.CharField(choices=[('1', 'Pembina Utama (IV/e)'), ('2', 'Pembina Utama Madya (IV/d)'), ('3', 'Pembina Utama Muda (IV/c)'), ('4', 'Pembina Tingkat I (IV/b)'), ('5', 'Pembina (IV/a)'), ('6', 'Penata Tingkat I (III/d)'), ('7', 'Penata (III/c)'), ('8', 'Penata Muda Tingkat I (III/b)'), ('9', 'Penata Muda (III/a)'), ('10', 'Pengatur Tingkat I (II/d)'), ('11', 'Pengatur (II/c)'), ('12', 'Pengatur Muda Tingkat I (II/b'), ('13', 'Pengatur Muda (II/a'), ('14', 'Juru Tingkat I (I/d'), ('15', 'Juru (I/c'), ('16', 'Juru Muda Tingkat I(I/b'), ('17', 'Juru Muda (I/a')], default='7', max_length=40),
        ),
    ]
