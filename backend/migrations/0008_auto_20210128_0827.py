# Generated by Django 3.1.5 on 2021-01-28 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_masterbutirkegiatan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterbutirkegiatan',
            name='butir_kegiatan_pranata_komputer',
            field=models.CharField(blank=True, choices=[('I.A.1.', 'I.A.1. Melakukan identifikasi dan analisis kebutuhan bisnis institusi'), ('I.A.2.', 'I.A.2. Melakukan reviu TI yang digunakan institusi saat ini atau tren TI terkini'), ('I.A.3.', 'I.A.3. Melakukan analisis terhadap strategi bisnis institusi yang berdampak pada strategi TI institusi'), ('I.A.4.', 'I.A.4. Melakukan analisis dampak TI yang digunakan institusi saat ini dan trennya terhadap perubahan strategi bisnis institusi'), ('I.A.5.', 'I.A.5. Menyusun kerangka kerja untuk penyusunan strategi TI'), ('I.A.6.', 'I.A.6. Melakukan pengkajian terhadap kerangka kerja untuk penyusunan strategi TI'), ('I.A.7.', 'I.A.7. Melakukan analisis kesenjangan terhadap strategi TI'), ('I.A.8.', 'I.A.8. Menyusun strategi TI'), ('I.A.9.', 'I.A.9. Melakukan pengkajian terhadap strategi TI'), ('I.A.10.', 'I.A.10. Menyusun komponen Enterprise Architecture (EA) saat ini'), ('I.A.11.', 'I.A.11. Menyusun pengembangan komponen Enterprise Architecture (EA) masa yang akan datang'), ('I.A.12.', 'I.A.12. Melakukan analisis kesenjangan terhadap komponen Enterprise Architecture (EA)'), ('I.A.13.', 'I.A.13. Melakukan pengkajian terhadap analisis kesenjangan terhadap komponen Enterprise Architecture (EA)'), ('I.A.14.', 'I.A.14. Membuat usulan roadmap pada masing-masing komponen Enterprise Architecture (EA)'), ('I.A.15.', 'I.A.15. Melakukan pengkajian terhadap usulan roadmap pada masing-masing komponen Enterprise Architecture (EA)'), ('I.A.16.', 'I.A.16. Menyusun strategi implementasi Enterprise Architecture (EA)'), ('I.A.17.', 'I.A.17. Melakukan pengkajian terhadap kelayakan strategi implementasi Enterprise Architecture (EA)'), ('I.A.18.', 'I.A.18. Menyusun atau mengkaji kerangka kerja tata kelola TI'), ('I.A.19.', 'I.A.19. Menyusun tata kelola TI'), ('I.A.20.', 'I.A.20. Melakukan pengkajian terhadap tata kelola TI'), ('I.A.21.', 'I.A.21. Menyusun struktur tata kelola TI'), ('I.A.22.', 'I.A.22. Menyusun atau mengkaji kerangka kerja kebijakan TI'), ('I.A.23.', 'I.A.23. Menyusun atau mengkaji kebijakan TI'), ('I.A.24.', 'I.A.24. Menyusun instrumen untuk mengukur keselarasan tujuan TI dan tujuan bisnis'), ('I.A.25.', 'I.A.25. Melakukan pengukuran dan pengkajian terhadap keselarasan tujuan TI dengan tujuan bisnis'), ('I.A.26.', 'I.A.26. Menetapkan target manfaat atau dampak dari implementasi TI'), ('I.A.27.', 'I.A.27. Melakukan evaluasi target manfaat atau dampak dari implementasi TI'), ('I.A.28.', 'I.A.28. Menetapkan cara mengukur performa TI'), ('I.A.29.', 'I.A.29. Melakukan pengukuran performa TI'), ('I.A.30.', 'I.A.30. Menyusun rencana TI'), ('I.A.31.', 'I.A.31. Menyusun revisi rencana TI'), ('I.A.32.', 'I.A.32. Menyusun skala prioritas solusi TI dalam Rencana TI'), ('I.A.33.', 'I.A.33. Menyusun rencana transformasi TI'), ('I.A.34.', 'I.A.34. Menyusun rencana transformasi TI'), ('I.A.35.', 'I.A.35. Menyusun rencana pembiayaan TI'), ('I.A.36.', 'I.A.36. Menyusun templat/pola acu untuk strategi operasional rencana TI'), ('I.A.37.', 'I.A.37. Melakukan pengkajian terhadap kelayakan implementasi rencana TI'), ('I.B.1.', 'I.B.1. Menyusun strategi layanan teknologi informasi'), ('I.B.2.', 'I.B.2. Mengelola kebutuhan layanan teknologi informasi'), ('I.B.3.', 'I.B.3. Menyusun portofolio layanan teknologi informasi'), ('I.B.4.', 'I.B.4. Mengelola portofolio layanan teknologi informasi'), ('I.B.5.', 'I.B.5. Mengelola anggaran layanan teknologi informasi'), ('I.B.6.', 'I.B.6. Menyusun SOP untuk kegiatan IT Service Management'), ('I.B.7.', 'I.B.7. Mengelola katalog layanan teknologi informasi'), ('I.B.8.', 'I.B.8. Mengelola penyedia jasa atau barang untuk layanan teknologi informasi'), ('I.B.9.', 'I.B.9. Mengelola kapasitas layanan teknologi informasi'), ('I.B.10.', 'I.B.10. Mengelola tingkat layanan teknologi informasi'), ('I.B.11.', 'I.B.11. Mengelola dukungan operasional layanan teknologi informasi'), ('I.B.12.', 'I.B.12. Melakukan pemantauan (monitoring) dan evaluasi ketersediaan layanan teknologi informasi'), ('I.B.13.', 'I.B.13. Menyusun perencanaan transisi layanan teknologi informasi'), ('I.B.14.', 'I.B.14. Mengelola perubahan layanan teknologi informasi'), ('I.B.15.', 'I.B.15. Mengelola aset dan konfigurasi layanan teknologi informasi'), ('I.B.16.', 'I.B.16. Mengelola pengetahuan layanan teknologi informasi'), ('I.B.17.', 'I.B.17. Melakukan validasi, pengujian, dan evaluasi layanan teknologi informasi'), ('I.B.18.', 'I.B.18. Mengelola rilis dan deployment layanan teknologi informasi'), ('I.B.19.', 'I.B.19. Mengelola event kegiatan teknologi informasi'), ('I.B.20.', 'I.B.20. Mengelola insiden kegiatan teknologi informasi'), ('I.B.21.', 'I.B.21. Mengelola permintaan dan layanan teknologi informasi'), ('I.C.1.', 'I.C.1. Menyusun atau mengelola strategi manajemen data instansi'), ('I.C.2.', 'I.C.2. Menyusun kebijakan data, standar data, atau prosedur pengelolaan data'), ('I.C.3.', 'I.C.3. Melakukan reviu kebijakan data, standar data, atau prosedur pengelolaan data'), ('I.C.4.', 'I.C.4. Menyusun rekomendasi persetujuan arsitektur data'), ('I.C.5.', 'I.C.5. Melakukan reviu rekomendasi persetujuan arsitektur data'), ('I.C.6.', 'I.C.6. Menyusun rencana kegiatan layanan pengelolaan data'), ('I.C.7.', 'I.C.7. Melakukan supervisi terhadap organisasi dan staf pengelola data'), ('I.C.8.', 'I.C.8. Menyusun alternatif solusi permasalahan pengelolaan data'), ('I.C.9.', 'I.C.9. Melakukan evaluasi pelaksanaan pengelolaan data'), ('I.C.10.', 'I.C.10. Menyusun bahan sosialisasi tentang pengelolaan data'), ('I.C.11.', 'I.C.11. Melakukan sosialisasi tentang pengelolaan data'), ('I.C.12.', 'I.C.12. Menyusun model data instansi'), ('I.C.13.', 'I.C.13. Melakukan analisis model data instansi'), ('I.C.14.', 'I.C.14. Menyusun arsitektur teknologi data'), ('I.C.15.', 'I.C.15. Menyusun arsitektur integrasi data'), ('I.C.16.', 'I.C.16. Melakukan perancangan data model'), ('I.C.17.', 'I.C.17. Melakukan implementasi data model'), ('I.C.18.', 'I.C.18. Melakukan perancangan business intelligence'), ('I.C.19.', 'I.C.19. Melakukan implementasi business intelligence'), ('I.C.20.', 'I.C.20. Menyusun taksonomi data'), ('I.C.21.', 'I.C.21. Menyusun arsitektur data'), ('I.C.22.', 'I.C.22. Menyusun standar metadata'), ('I.C.23.', 'I.C.23. Melakukan pengumpulan kebutuhan informasi'), ('I.C.24.', 'I.C.24. Melakukan analisis kebutuhan informasi'), ('I.C.25.', 'I.C.25. Melakukan perancangan layanan akses data'), ('I.C.26.', 'I.C.26. Melakukan implementasi rancangan layanan akses data'), ('I.C.27.', 'I.C.27. Menyusun prosedur pengujian rancangan layanan akses data'), ('I.C.28.', 'I.C.28. Melakukan perancangan integrasi data'), ('I.C.29.', 'I.C.29. Melakukan ingestion data'), ('I.C.30.', 'I.C.30. Melakukan implementasi rancangan integrasi data'), ('I.C.31.', 'I.C.31. Menyusun prosedur pengujian rancangan integrasi data'), ('I.C.32.', 'I.C.32. Melakukan evaluasi hasil pengujian rancangan integrasi data'), ('I.C.33.', 'I.C.33. Menyusun prosedur pengujian validasi kebutuhan informasi'), ('I.C.34.', 'I.C.34. Melakukan evaluasi hasil pengujian prosedur validasi kebutuhan informasi'), ('I.C.35.', 'I.C.35. Melakukan validasi kebutuhan informasi'), ('I.C.36.', 'I.C.36. Menyusun dokumentasi rancangan database'), ('I.C.37.', 'I.C.37. Melakukan instalasi dan konfigurasi DBMS'), ('I.C.38.', 'I.C.38. Menyusun rencana backup dan pemulihan data'), ('I.C.39.', 'I.C.39. Melakukan backup atau pemulihan data'), ('I.C.40.', 'I.C.40. Menyusun tingkat kinerja layanan database'), ('I.C.41.', 'I.C.41. Melakukan peningkatan kinerja database'), ('I.C.42.', 'I.C.42. Menyusun rencana retensi data'), ('I.C.43.', 'I.C.43. Menyusun kebutuhan teknologi data'), ('I.C.44.', 'I.C.44. Melakukan evaluasi teknologi data'), ('I.C.45.', 'I.C.45. Melakukan pengadministrasian teknologi data'), ('I.C.46.', 'I.C.46. Melakukan deteksi dan perbaikan terhadap permasalahan teknologi data'), ('I.C.47.', 'I.C.47. Melakukan implementasi data mining'), ('I.C.48.', 'I.C.48. Menyusun kebutuhan atau standar keamanan data'), ('I.C.49.', 'I.C.49. Menyusun kebijakan keamanan data'), ('I.C.50.', 'I.C.50. Menyusun definisi kontrol atau prosedur keamanan data'), ('I.C.51.', 'I.C.51. Mengelola pengguna dan hak akses data'), ('I.C.52.', 'I.C.52. Melakukan analisis perilaku akses pengguna'), ('I.C.53.', 'I.C.53. Menyusun pemetaan data berdasarkan tingkat kerahasiaan informasi'), ('I.D.1.', 'I.C.1. Melakukan studi kelayakan audit TI'), ('I.D.2.', 'I.C.2. Menyusun proposal audit TI'), ('I.D.3.', 'I.C.3. Melakukan perancangan proses bisnis dan SOP pelaksanaan audit TI'), ('I.D.4.', 'I.C.4. Melakukan pengkajian terhadap framework audit TI'), ('I.D.5.', 'I.C.5. Melakukan pengkajian terhadap tool dan aplikasi yang digunakan untuk audit TI'), ('I.D.6.', 'I.C.6. Melakukan analisis awal untuk kebutuhan audit TI'), ('I.D.7.', 'I.C.7. Melakukan pengumpulan data audit TI menggunakan metode tertentu'), ('I.D.8.', 'I.C.8. Melakukan pengujian, verifikasi, atau validasi terhadap data audit TI'), ('I.D.9.', 'I.C.9. Melakukan analisis data audit TI'), ('I.D.10.', 'I.C.10. Melakukan evaluasi kegiatan audit TI'), ('I.E.1.', 'I.E.1. Melakukan reviu dokumen manajemen risiko'), ('I.E.2.', 'I.E.2. Membuat framework manajemen risiko'), ('I.E.3.', 'I.E.3. Menyusun rencana manajemen risiko'), ('I.E.4.', 'I.E.4. Melakukan analisis faktor risiko'), ('I.E.5.', 'I.E.5. Melakukan identifikasi risiko'), ('I.E.6.', 'I.E.6. Melakukan pengukuran risiko'), ('I.E.7.', 'I.E.7. Menyusun strategi penanganan risiko'), ('I.E.8.', 'I.E.8. Membuat prosedur penanganan risiko'), ('I.E.9.', 'I.E.9. Menyusun solusi teknis penanganan risiko'), ('I.E.10.', 'I.E.10. Melakukan pemantauan (monitoring) terhadap strategi penanganan risiko'), ('I.E.11.', 'I.E.11. Melakukan evaluasi terhadap strategi penanganan risiko'), ('II.A.1.', 'II.A.1. Melakukan analisis kebutuhan pengguna sistem jaringan komputer kompleks'), ('II.A.2.', 'II.A.2. Melakukan analisis kondisi sistem jaringan komputer kompleks yang sedang berjalan'), ('II.A.3.', 'II.A.3. Membuat rancangan logis (logical design) sistem jaringan komputer'), ('II.A.4.', 'II.A.4. Membuat rancangan fisik (physical design) sistem jaringan komputer'), ('II.A.5.', 'II.A.5. Menerapkan rancangan fisik sistem jaringan komputer kompleks'), ('II.A.6.', 'II.A.6. Menerapkan rancangan logis sistem pengamanan jaringan komputer kompleks'), ('II.A.7.', 'II.A.7. Menyusun prosedur pemanfaatan sistem jaringan'), ('II.A.8.', 'II.A.8. Menyusun rancangan uji coba sistem jaringan kompleks'), ('II.A.9.', 'II.A.9. Melakukan uji coba sistem jaringan komputer kompleks'), ('II.A.10.', 'II.A.10. Melakukan evaluasi uji coba sistem jaringan komputer sederhana'), ('II.A.11.', 'II.A.11. Melakukan evaluasi uji coba sistem jaringan komputer kompleks'), ('II.A.12.', 'II.A.12. Menyusun dokumentasi penggunaan sistem jaringan komputer'), ('II.A.13.', 'II.A.13. Melakukan analisis permasalahan dari hasil pemantauan (monitoring) jaringan'), ('II.A.14.', 'II.A.14. Melakukan optimalisasi sistem jaringan'), ('II.A.15.', 'II.A.15. Melakukan deteksi dan atau perbaikan terhadap permasalahan yang terjadi pada sistem jaringan kompleks'), ('II.A.16.', 'II.A.16. Menyusun rumusan kebijakan keamanan jaringan'), ('II.A.17.', 'II.A.17. Melakukan reviu kebijakan keamanan jaringan'), ('II.A.18.', 'II.A.18. Menyusun prosedur keamanan jaringan'), ('II.A.19.', 'II.A.19. Menyusun petunjuk teknis sistem jaringan komputer dan keamanan jaringan'), ('II.A.20.', 'II.A.20. Melakukan pemeriksaan kepatuhan terhadap kebijakan keamanan jaringan'), ('II.B.1.', 'II.B.1. Menyusun rencana pengoperasian infrastruktur TI'), ('II.B.2.', 'II.B.2. Menyusun KAK'), ('II.B.3.', 'II.B.3. Melakukan evaluasi proposal teknis penyedia barang/jasa infrastruktur TI'), ('II.B.4.', 'II.B.4. Melakukan pengkajian terhadap pemenuhan/ kesesuaian infrastruktur TI terhadap regulasi'), ('II.B.5.', 'II.B.5. Melakukan pemeriksaan kesesuaian antara Infrastruktur TI dengan spesifikasi teknis'), ('II.B.6.', 'II.B.6. Melakukan pengujian infrastruktur TI'), ('II.B.7.', 'II.B.7. Menyusun rencana pemeliharaan infrastruktur TI'), ('II.B.8.', 'II.B.8. Melakukan pemeliharaan infrastruktur TI'), ('II.B.9.', 'II.B.9. Melakukan pemasangan infrastruktur TI'), ('II.B.10.', 'II.B.10. Melakukan pengaturan akses keamanan fisik TI'), ('II.B.11.', 'II.B.11. Melakukan analisis permasalahan dari hasil pemantauan (monitoring) kinerja infrastruktur TI'), ('II.B.12.', 'II.B.12. Melakukan deteksi dan atau perbaikan terhadap permasalahan infrastruktur TI'), ('II.B.13.', 'II.B.13. Menyusun prosedur pemanfaatan infrastruktur TI'), ('II.B.14.', 'II.B.14. Menyiapkan peralatan video conference (vicon/streaming), monitoring peralatan (audio, video, dan perangkat jaringan), dan mengatur layout'), ('II.B.15.', 'II.B.15. Melakukan optimalisasi kinerja infrastruktur TI'), ('III.A.1.', 'III.A.1. Menyusun usulan pembangunan sistem informasi'), ('III.A.2.', 'III.A.2. Menyusun rencana studi kelayakan sistem informasi'), ('III.A.3.', 'III.A.3. Melakukan studi kelayakan sistem informasi'), ('III.A.4.', 'III.A.4. Melakukan identifikasi kebutuhan pengguna sistem informasi'), ('III.A.5.', 'III.A.5. Melakukan analisis sistem informasi'), ('III.A.6.', 'III.A.6. Melakukan pemodelan proses sistem informasi'), ('III.A.7.', 'III.A.7. Melakukan perancangan sistem informasi'), ('III.A.8.', 'III.A.8. Membuat algoritma pemrograman'), ('III.A.9.', 'III.A.9. Membuat program aplikasi / sistem informasi'), ('III.A.10.', 'III.A.10. Mengembangkan program aplikasi sistem informasi'), ('III.A.11.', 'III.A.11. Menyusun definisi rule validasi pada program aplikasi sistem informasi'), ('III.A.12.', 'III.A.12. Melakukan penyiapan data untuk uji coba sistem informasi'), ('III.A.13.', 'III.A.13. Menyusun skenario uji coba sistem informasi'), ('III.A.14.', 'III.A.14. Melakukan uji coba sistem informasi'), ('III.A.15.', 'III.A.15. Melakukan pemeriksaan dan analisis hasil uji coba sistem informasi'), ('III.A.16.', 'III.A.16. Melakukan deteksi dan atau perbaikan kerusakan sistem informasi'), ('III.A.17.', 'III.A.17. Menyusun petunjuk operasional  program  aplikasi sistem informasi'), ('III.A.18.', 'III.A.18. Menyusun dokumentasi pengembangan sistem informasi'), ('III.A.19.', 'III.A.19. Melakukan instalasi/upgrade dan konfigurasi sistem operasi/aplikasi'), ('III.A.20.', 'III.A.20. Melakukan pemantauan (monitoring) kinerja aplikasi sistem informasi di lingkungan instansi'), ('III.B.1.', 'III.B.1. Menyusun rencana studi kelayakan untuk pengolahan data'), ('III.B.2.', 'III.B.2. Melakukan studi kelayakan untuk pengolahan data'), ('III.B.3.', 'III.B.3. Menyusun prosedur pengolahan data'), ('III.B.4.', 'III.B.4. Menyusun petunjuk teknis pelaksanaan pengolahan data'), ('III.B.5.', 'III.B.5. Melakukan  data crawling, data feeding, atau data loading'), ('III.B.6.', 'III.B.6. Melakukan manipulasi data'), ('III.B.7.', 'III.B.7. Melakukan pemantauan (monitoring) pengolahan data'), ('III.B.8.', 'III.B.8. Melakukan evaluasi pengolahan data'), ('III.C.1.', 'III.C.1. Menyusun definisi sistem proyeksi pada suatu data spasial'), ('III.C.2.', 'III.C.2. Membuat peta tematik rinci'), ('III.C.3.', 'III.C.3. Melakukan pengolahan data atribut dan spasial rinci'), ('III.C.4.', 'III.C.4. Melakukan analisis data spasial'), ('III.C.5.', 'III.C.5. Mengoperasikan tools untuk membuat storyboard'), ('III.C.6.', 'III.C.6. Membuat flowchart untuk pemrograman multimedia'), ('III.C.7.', 'III.C.7. Melakukan editing objek multimedia kompleks dengan piranti lunak'), ('III.C.8.', 'III.C.8. Membuat objek multimedia kompleks dengan piranti lunak'), ('III.C.9.', 'III.C.9. Membuat prototype kompleks pada program multimedia'), ('III.C.10.', 'III.C.10. Membuat program multimedia kompleks'), ('III.C.11.', 'III.C.11. Menyusun skenario uji coba program multimedia'), (None, '----- Bukan Kegiatan Pranata Komputer -----')], max_length=180),
        ),
    ]
