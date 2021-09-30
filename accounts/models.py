from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class CustomUser(AbstractUser):
    pass

    PANGKAT_GOLONGAN_CHOICES = [
        ('1', 'Pembina Utama (IV/e)'),
        ('2', 'Pembina Utama Madya (IV/d)'),
        ('3', 'Pembina Utama Muda (IV/c)'),
        ('4', 'Pembina Tingkat I (IV/b)'),
        ('5', 'Pembina (IV/a)'),
        ('6', 'Penata Tingkat I (III/d)'),
        ('7', 'Penata (III/c)'),
        ('8', 'Penata Muda Tingkat I (III/b)'),
        ('9', 'Penata Muda (III/a)'),
        ('10', 'Pengatur Tingkat I (II/d)'),
        ('11', 'Pengatur (II/c)'),
        ('12', 'Pengatur Muda Tingkat I (II/b)'),
        ('13', 'Pengatur Muda (II/a)'),
        ('14', 'Juru Tingkat I (I/d)'),
        ('15', 'Juru (I/c)'),
        ('16', 'Juru Muda Tingkat I(I/b)'),
        ('17', 'Juru Muda (I/a)'),
    ]

    JABATAN_KANTOR_CHOICES = [
        ('1', 'Kepala BPS'),
        ('2', 'Kepala Subbagian Umum'),
        ('3', 'Koordinator Fungsi Statistik Sosial'),
        ('4', 'Koordinator Fungsi Statistik Produksi'),
        ('5', 'Koordinator Fungsi Statistik Distribusi'),
        ('6', 'Koordinator Fungsi Neraca Wilayah dan Analisis Statistik'),
        ('7', 'Koordinator Fungsi Integrasi Pengolahan dan Diseminasi Statistik'),
        ('8', 'Staf Subbagian Umum'),
        ('9', 'Staf Fungsi Statistik Sosial'),
        ('10', 'Staf Fungsi Statistik Produksi'),
        ('11', 'Staf Fungsi Statistik Distribusi'),
        ('12', 'Staf Fungsi Neraca Wilayah dan Analisis Statistik'),
        ('13', 'Staf Fungsi Integrasi Pengolahan dan Diseminasi Statistik'),
        ('14', 'KSK Kuantan Mudik'),
        ('15', 'KSK Hulu Kuantan'),
        ('16', 'KSK Gunung Toar'),
        ('17', 'KSK Pucuk Rantau'),
        ('18', 'KSK Singingi'),
        ('19', 'KSK Singingi Hilir'),
        ('20', 'KSK Kuantan Tengah'),
        ('21', 'KSK Sentajo Raya'),
        ('22', 'KSK Benai'),
        ('23', 'KSK Kuantan Hilir'),
        ('24', 'KSK Pangean'),
        ('25', 'KSK Logas Tanah Darat'),
        ('26', 'KSK Kuantan Hilir Seberang'),
        ('27', 'KSK Cerenti'),
        ('28', 'KSK Inuman'),
    ]

    JABATAN_FUNGSIONAL_CHOICES = [
        ('0', 'Fungsional Umum'),
        ('1', 'Statistisi Pelaksana'),
        ('2', 'Statistisi Pelaksana Lanjutan'),
        ('3', 'Statistisi Penyelia'),
        ('4', 'Statistisi Pertama'),
        ('5', 'Statistisi Muda'),
        ('6', 'Statistisi Madya'),
        ('7', 'Statistisi Utama'),
        ('8', 'Pranata Komputer Terampil'),
        ('9', 'Pranata Komputer Mahir'),
        ('10', 'Pranata Komputer Penyelia'),
        ('11', 'Pranata Komputer Ahli Pertama'),
        ('12', 'Pranata Komputer Ahli Muda'),
        ('13', 'Pranata Komputer Ahli Madya'),
        ('14', 'Pranata Komputer Ahli Utama'),
    ]

    KASI_LIST = ['1','2','3','4','5','6','7']

    pangkat_golongan = models.CharField(
        max_length=40,
        choices=PANGKAT_GOLONGAN_CHOICES,
        default='7',
    )

    jabatan_kantor = models.CharField(
        max_length=80,
        choices=JABATAN_KANTOR_CHOICES,
        default='7',
    )

    jabatan_fungsional = models.CharField(
        max_length=50,
        choices=JABATAN_FUNGSIONAL_CHOICES,
        default='12',
    )

    nip = models.CharField(max_length=18, default='199212052014121001')
    nip_lama = models.CharField(max_length=9, default='340057019')
    no_hp = models.CharField(max_length=14, default='081316658226')

    foto_profil = models.ImageField(default="default.jpg", upload_to='foto_profil')

    def get_jabatan_kantor_dropdown():
        values = [x[0] for x in CustomUser.JABATAN_KANTOR_CHOICES]
        choices = [x[1] for x in CustomUser.JABATAN_KANTOR_CHOICES]
        return zip(values, choices)

    def get_jabatan_kantor_singkat(self):
        singkat = self.get_jabatan_kantor_display()
        if singkat == 'Koordinator Fungsi Integrasi Pengolahan dan Diseminasi Statistik' or singkat == 'Staf Fungsi Integrasi Pengolahan dan Diseminasi Statistik':
            return 'IPDS'
        elif singkat == 'Koordinator Fungsi Neraca Wilayah dan Analisis Statistik' or singkat == 'Staf Fungsi Neraca Wilayah dan Analisis Statistik':
            return 'Neraca Wilayah dan Analisis Statistik'
        else:
            return " ".join(singkat.split()[1:])

        # return " ".join(singkat.split()[1:])

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.foto_profil.path)
        width, height = img.size  # Get dimensions 

        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))
        
        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
        
        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 300 and height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

        img.save(self.foto_profil.path)
