# Generated by Django 3.1.5 on 2021-01-28 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0009_auto_20210128_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterkegiatan',
            name='subject_matter',
            field=models.CharField(choices=[('1', 'Kepala BPS'), ('2', 'Kepala Subbagian Umum'), ('3', 'Koordinator Fungsi Statistik Sosial'), ('4', 'Koordinator Fungsi Statistik Produksi'), ('5', 'Koordinator Fungsi Statistik Distribusi'), ('6', 'Koordinator Fungsi Neraca Wilayah dan Analisis Statistik'), ('7', 'Koordinator Fungsi Integrasi Pengolahan dan Diseminasi Statistik'), ('8', 'Staf'), ('9', 'KSK Kuantan Mudik'), ('10', 'KSK Hulu Kuantan'), ('11', 'KSK Gunung Toar'), ('12', 'KSK Pucuk Rantau'), ('13', 'KSK Singingi'), ('14', 'KSK Singingi Hilir'), ('15', 'KSK Kuantan Tengah'), ('16', 'KSK Sentajo Raya'), ('17', 'KSK Benai'), ('18', 'KSK Kuantan Hilir'), ('19', 'KSK Pangean'), ('20', 'KSK Logas Tanah Darat'), ('21', 'KSK Kuantan Hilir Seberang'), ('22', 'KSK Cerenti'), ('23', 'KSK Inuman')], default='7', max_length=80),
        ),
        migrations.CreateModel(
            name='DokumenCKP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periode', models.DateTimeField(null=True)),
                ('pegawai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ButirCKP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_butir_ckp', models.CharField(choices=[('UTAMA', 'Utama'), ('TAMBAHAN', 'Tambahan')], max_length=10)),
                ('target', models.IntegerField()),
                ('realisasi', models.IntegerField(blank=True)),
                ('tingkat_kualitas', models.FloatField(blank=True)),
                ('keterangan', models.TextField()),
                ('dokumen_ckp', models.ManyToManyField(to='backend.DokumenCKP')),
                ('kegiatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.masterkegiatan')),
            ],
        ),
    ]
