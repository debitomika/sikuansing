from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from accounts.models import CustomUser
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import locale

# Kelas untuk menyimpan daftar master butir kegiatan statisti dan prakom
class MasterButirKegiatan(models.Model):

    JENIS_FUNGSIONAL_CHOICES = [
        ('ST', 'Statistisi'),
        ('PR', 'Pranata Komputer'),
        (None, '----- Bukan Kegiatan Fungsional -----'),
    ]

    UNSUR_STATISTISI_CHOICES = [
        ('I.', 'I. Pendidikan'),
        ('II.', 'II. Penyediaan Data dan Informasi Statistik'),
        ('III.', 'III. Analisis dan Pengembangan Statistik'),
        ('IV.', 'IV. Pengembangan Profesi Statistisi'),
        ('V.', 'V. Pendukung Kegiatan Statistisi'),
        (None, '----- Bukan Kegiatan Statistisi -----'),
    ]

    SUB_UNSUR_STATISTISI_CHOICES = [
        ('I.A.', 'I.A. Pendidikan Sekolah dan Memperoleh Ijazah/Gelar'),
        ('I.B.', 'I.B. Pendidikan dan Pelatihan Fungsional di Bidang Statistik Serta Memperoleh Surat Tanda Tamat Pendidikan dan Pelatihan/Sertifikat'),
        ('I.C.', 'I.C. Pendidikan dan Pelatihan Prajabatan'),
        ('II.A.', 'II.A. Persiapan'),
        ('II.B.', 'II.B. Pengumpulan Data'),
        ('II.C.', 'II.C. Pengolahan'),
        ('II.D.', 'II.D. Penyajian dan Publikasi'),
        ('III.A.', 'III.A. Analisis Statistik'),
        ('III.B.', 'III.B. Pengembangan Statistik'),
        ('IV.A.', 'IV.A. Pembuatan Karya Tulis/Karya Ilmiah di Bidang Statistik'),
        ('IV.B.', 'IV.B. Penyusunan Petunjuk Teknis Pelaksanaan Pengelolaan Kegiatan Statistik'),
        ('IV.C.', 'IV.C. Penerjemahan/Penyaduran Buku atau Karya Ilmiah di Bidang Statistik'),
        ('V.A.', 'V.A. Memberikan Bimbingan Penuh Kader Statistisi'),
        ('V.B.', 'V.B. Pengajaran/Pelatihan di Bidang Statistik'),
        ('V.C.', 'V.C. Peran Serta dalam Mengikuti Seminar/Lokakarya/Konferensi'),
        ('V.D.', 'V.D. Keanggotaan dalam Tim Penilai Jabatan Fungsional Statistisi'),
        ('V.E.', 'V.E. Keanggotaan dalam Organisasi Profesi'),
        ('V.F.', 'V.F. Perolahan Piagam Kehormatan'),
        ('V.G.', 'V.G. Perolahan Gelar Kesarjanaan Lainnya'),
        (None, '----- Bukan Kegiatan Statistisi -----'),
    ]

    BUTIR_KEGIATAN_STATISTISI_CHOICES = [
        ('I.A.1.', 'I.A.1. Pendidikan Sekolah dan Memperoleh Ijazah/Gelar Doktor/Spesialis II (S3)'),
        ('I.A.2.', 'I.A.2. Pendidikan Sekolah dan Memperoleh Ijazah/Gelar Magister/Spesialis I (S2)'),
        ('I.A.3.', 'I.A.3. Pendidikan Sekolah dan Memperoleh Ijazah/Gelar Sarjana (S1)/Diploma IV'),
        ('I.B.1.', 'I.B.1. Pendidikan dan Pelatihan Fungsional di Bidang Statistik Serta Memperoleh Surat Tanda Tamat Pendidikan dan Pelatihan/Sertifikat Lamanya Lebih dari 960 Jam'),
        ('I.B.2.', 'I.B.2. Pendidikan dan Pelatihan Fungsional di Bidang Statistik Serta Memperoleh Surat Tanda Tamat Pendidikan dan Pelatihan/Sertifikat Lamanya antara 641-960 Jam'),
        ('I.B.3.', 'I.B.3. Pendidikan dan Pelatihan Fungsional di Bidang Statistik Serta Memperoleh Surat Tanda Tamat Pendidikan dan Pelatihan/Sertifikat Lamanya antara 401-640 Jam'),
        ('I.B.4.', 'I.B.4. Pendidikan dan Pelatihan Fungsional di Bidang Statistik Serta Memperoleh Surat Tanda Tamat Pendidikan dan Pelatihan/Sertifikat Lamanya antara 161-400 Jam'),
        ('I.B.5.', 'I.B.5. Pendidikan dan Pelatihan Fungsional di Bidang Statistik Serta Memperoleh Surat Tanda Tamat Pendidikan dan Pelatihan/Sertifikat Lamanya antara 81-160 Jam'),
        ('I.B.6.', 'I.B.6. Pendidikan dan Pelatihan Fungsional di Bidang Statistik Serta Memperoleh Surat Tanda Tamat Pendidikan dan Pelatihan/Sertifikat Lamanya antara 31-80 Jam'),
        ('I.B.7.', 'I.B.7. Pendidikan dan Pelatihan Fungsional di Bidang Statistik Serta Memperoleh Surat Tanda Tamat Pendidikan dan Pelatihan/Sertifikat Lamanya antara 10-30 Jam'),
        ('I.C.', 'I.C. Pendidikan dan Pelatihan Prajabatan Golongan III'),
        ('II.A.1.', 'II.A.1. Mengumpulkan Bahan/Informasi Pendukung untuk Kegiatan Statistik'),
        ('II.A.2.', 'II.A.2. Menelaah Bahan/Informasi Pendukung untuk Kegiatan Statistik'),
        ('II.A.3.', 'II.A.3. Membuat Rencana Tabulasi Kegiatan Statistik'),
        ('II.A.4.', 'II.A.4. Mengikuti Pembahasan Kuesioner dan Instrumen lainnya pada Kegiatan Statistik'),
        ('II.A.5.', 'II.A.5. Mengikuti Pembahasan Penyusunan Pedoman Kegiatan Statistik'),
        ('II.A.6.a.', 'II.A.6.a. Melaksanakan Kegiatan Sampling: Menyusun Kerangka Sampel'),
        ('II.A.6.b.', 'II.A.6.b. Melaksanakan Kegiatan Sampling: Menyusun Metode Pemilihan Sampel'),
        ('II.A.6.c.', 'II.A.6.c. Melaksanakan Kegiatan Sampling: Membuat Program Pemilihan Sampel'),
        ('II.A.6.d.', 'II.A.6.d. Melaksanakan Kegiatan Sampling: Memilih Sampel'),
        ('II.A.6.e.', 'II.A.6.e. Melaksanakan Kegiatan Sampling: Memperbaharui (updating) Kerangka Sampel'),
        ('II.A.7.a.', 'II.A.7.a. Melaksanakan Kegiatan dalam Lingkup Observasi: Penyusunan Kerangka Sampel'),
        ('II.A.7.b.', 'II.A.7.b. Melaksanakan Kegiatan dalam Lingkup Observasi: Monitoring dan Evaluasi Penerimaan Daftar Sampel'),
        ('II.A.7.c.', 'II.A.7.c. Melaksanakan Kegiatan dalam Lingkup Observasi: Pengelolaan dan Penyempurnaan Master File'),
        ('II.A.7.d.', 'II.A.7.d. Melaksanakan Kegiatan dalam Lingkup Observasi: Penentuan Metode Penarikan Sampel'),
        ('II.A.8.', 'II.A.8. Menghitung Sampling Error Kegiatan Statistik'),
        ('II.A.9.', 'II.A.9. Menghitung Penimbang dalam Rangka Estimasi Kegiatan Statistik'),
        ('II.A.10.', 'II.A.10. Mengatur alokasi dokumen/peralatan/sensus/survei/observasi tingkat nasional'),
        ('II.A.11.', 'II.A.11. Mengikuti pelatihan pengumpulan data'),
        ('II.A.12.', 'II.A.12. Memberikan pelatihan pengumpulan data bagi petugas'),
        ('II.A.13.', 'II.A.13. Membuat peta indeks kegiatan statistik'),
        ('II.A.14.', 'II.A.14. Meneliti peta analog observasi (manual)'),
        ('II.A.15.', 'II.A.15. Meneliti peta indeks kegiatan statistik'),
        ('II.A.16.', 'II.A.16. Membuat peta digital'),
        ('II.A.17.', 'II.A.17. Mengelola peta digital'),
        ('II.A.18.', 'II.A.18. Melakukan pengawasan pemetaan'),
        ('II.A.19.a.', 'II.A.19.a. Memeriksa hasil penarikan sampel kegiatan observasi berdasarkan: Wilayah Kerja'),
        ('II.A.19.b.', 'II.A.19.b. Memeriksa hasil penarikan sampel kegiatan observasi berdasarkan: Non Wilayah Kerja'),
        ('II.B.1.a.', 'II.B.1.a. Melakukan pengumpulan data pada kegiatan statistik objek rumah tangga: kuesioner sederhana'),
        ('II.B.1.b.', 'II.B.1.b. Melakukan pengumpulan data pada kegiatan statistik objek rumah tangga: kuesioner sedang'),
        ('II.B.1.c.', 'II.B.1.c. Melakukan pengumpulan data pada kegiatan statistik objek rumah tangga: kuesioner kompleks'),
        ('II.B.2.a.', 'II.B.2.a. Melakukan pengumpulan data pada kegiatan statistik objek non rumah tangga: kuesioner sederhana'),
        ('II.B.2.b.', 'II.B.2.b. Melakukan pengumpulan data pada kegiatan statistik objek non rumah tangga: kuesioner sedang'),
        ('II.B.2.c.', 'II.B.2.c. Melakukan pengumpulan data pada kegiatan statistik objek non rumah tangga: kuesioner kompleks'),
        ('II.B.3.a.', 'II.B.3.a. Melakukan pengawasan pada kegiatan statistik objek rumah tangga: kuesioner sederhana'),
        ('II.B.3.b.', 'II.B.3.b. Melakukan pengawasan pada kegiatan statistik objek rumah tangga: kuesioner sedang'),
        ('II.B.3.c.', 'II.B.3.c. Melakukan pengawasan pada kegiatan statistik objek rumah tangga: kuesioner kompleks'),
        ('II.B.4.a.', 'II.B.4.a. Melakukan pengawasan pada kegiatan statistik objek non rumah tangga: kuesioner sederhana'),
        ('II.B.4.b.', 'II.B.4.b. Melakukan pengawasan pada kegiatan statistik objek non rumah tangga: kuesioner sedang'),
        ('II.B.4.c.', 'II.B.4.c. Melakukan pengawasan pada kegiatan statistik objek non rumah tangga: kuesioner kompleks'),
        ('II.B.5.a.', 'II.B.5.a. Melakukan pemeriksaan hasil pengumpulan data objek rumah tangga: kuesioner sederhana'),
        ('II.B.5.b.', 'II.B.5.b. Melakukan pemeriksaan hasil pengumpulan data objek rumah tangga: kuesioner sedang'),
        ('II.B.5.c.', 'II.B.5.c. Melakukan pemeriksaan hasil pengumpulan data objek rumah tangga: kuesioner kompleks'),
        ('II.B.6.a.', 'II.B.6.a. Melakukan pemeriksaan hasil pengumpulan data objek non rumah tangga: kuesioner sederhana'),
        ('II.B.6.b.', 'II.B.6.b. Melakukan pemeriksaan hasil pengumpulan data objek non rumah tangga: kuesioner sedang'),
        ('II.B.6.c.', 'II.B.6.c. Melakukan pemeriksaan hasil pengumpulan data objek non rumah tangga: kuesioner kompleks'),
        ('II.C.1.a.', 'II.C.1.a. Merancang dan membuat pedoman pengolahan kegiatan statistik untuk: tabulasi'),
        ('II.C.1.b.', 'II.C.1.b. Merancang dan membuat pedoman pengolahan kegiatan statistik untuk: penyutingan dan penyandian hasil pengumpulan data'),
        ('II.C.1.c.', 'II.C.1.c. Merancang dan membuat pedoman pengolahan kegiatan statistik untuk: validitas data'),
        ('II.C.2.', 'II.C.2. Membuat program entri data tanpa validasi'),
        ('II.C.3.', 'II.C.3. Membuat program entri data dengan validasi hasil kegiatan statistik'),
        ('II.C.4.', 'II.C.4. Melakukan penyuntingan (editing), hasil kegiatan in depth interview'),
        ('II.C.5.', 'II.C.5. Membuat program tabulasi pada kegiatan statistik'),
        ('II.C.6.', 'II.C.6. Melakukan reformat data sensus/survei dari satu format ke format lainnya dalam media komputer'),
        ('II.D.1.', 'II.D.1. Membuat peta tematik digital kegiatan statistik'),
        ('II.D.2.a.', 'II.D.2.a. Memeriksa tabel/grafik hasil kegiatan statistik yang akan disajikan untuk publikasi: Tingkat kabupaten/kota'),
        ('II.D.2.b.', 'II.D.2.b. Memeriksa tabel/grafik hasil kegiatan statistik yang akan disajikan untuk publikasi: Tingkat provinsi'),
        ('II.D.2.c.', 'II.D.2.c. Memeriksa tabel/grafik hasil kegiatan statistik yang akan disajikan untuk publikasi: Tingkat nasional'),
        ('II.D.3.a.', 'II.D.3.a. Menyusun publikasi statistik: Tingkat Kabupaten/Kota'),
        ('II.D.3.b.', 'II.D.3.b. Menyusun publikasi statistik: Tingkat Provinsi'),
        ('II.D.3.c.', 'II.D.3.c. Menyusun publikasi statistik: Tingkat Nasional'),
        ('II.D.4.a.', 'II.D.4.a. Menyusun ringkasan eksekutif: Tingkat Kabupaten/Kota'),
        ('II.D.4.b.', 'II.D.4.b. Menyusun ringkasan eksekutif: Tingkat Provinsi'),
        ('II.D.4.c.', 'II.D.4.c. Menyusun ringkasan eksekutif: Tingkat Nasional'),
        ('II.D.5.', 'II.D.5. Menyusun publikasi digital dari kegiatan statistik'),
        ('II.D.6.', 'II.D.6. Menyajikan metadata statistik'),
        ('III.A.1.', 'III.A.1. Mengkaji kegiatan statistik'),
        ('III.A.2.', 'III.A.2. Membuat inovasi statistik dalam rangka penyusunan kegiatan statistik'),
        ('III.A.3.', 'III.A.3. Membuat estimasi parameter dalam rangka penyusunan statistik kelembagaan'),
        ('III.A.4.', 'III.A.4. Membuat outline untuk publikasi'),
        ('III.A.5.', 'III.A.5. Mengumpulkan literature/referensi untuk publikasi'),
        ('III.A.6.', 'III.A.6. Melakukan analisis sederhana lintas sektor'),
        ('III.A.7.a.', 'III.A.7.a. Melakukan analisis mendalam satu sektor'),
        ('III.A.7.b.', 'III.A.7.b. Melakukan analisis mendalam lintas sektor'),
        ('III.A.8.', 'III.A.8. Melakukan kajian lengkap terhadap organisasi dan lingkungan organisasi dalam rangka menentukan kebutuhan organisasi terhadap statistik'),
        ('III.B.1.', 'III.B.1. Mengembangkan metodologi kegiatan statistik'),
        ('III.B.2.a.', 'III.B.2.a. Memberikan konsultasi statistik dalam rangka penyusunan statistik kelembagaan: Menengah'),
        ('III.B.2.b.', 'III.B.2.b. Memberikan konsultasi statistik dalam rangka penyusunan statistik kelembagaan: Lanjutan'),
        ('III.B.2.c.', 'III.B.2.c. Memberikan konsultasi statistik dalam rangka penyusunan statistik kelembagaan: Khusus'),
        ('III.B.3.a.', 'III.B.3.a. Menyiapkan materi pengarahan statistik: Dasar'),
        ('III.B.3.b.', 'III.B.3.b. Menyiapkan materi pengarahan statistik: Menengah'),
        ('III.B.3.c.', 'III.B.3.c. Menyiapkan materi pengarahan statistik: Lanjutan'),
        ('III.B.3.d.', 'III.B.3.d. Menyiapkan materi pengarahan statistik: Khusus'),
        ('III.B.4.a.', 'III.B.4.a. Memberikan pengarahan statistik dalam rangka penyusunan statistik kelembagaan: Dasar'),
        ('III.B.4.b.', 'III.B.4.b. Memberikan pengarahan statistik dalam rangka penyusunan statistik kelembagaan: Menengah'),
        ('III.B.4.c.', 'III.B.4.c. Memberikan pengarahan statistik dalam rangka penyusunan statistik kelembagaan: Lanjutan'),
        ('III.B.4.d.', 'III.B.4.d. Memberikan pengarahan statistik dalam rangka penyusunan statistik kelembagaan: Khusus'),
        ('III.B.5.a.', 'III.B.5.a. Melakukan penyebarluasan hasil pengumpulan data statistik dalam rangka evaluasi kegiatan kelembagaaan dalam bidang statistik: Menengah'),
        ('III.B.5.b.', 'III.B.5.b. Melakukan penyebarluasan hasil pengumpulan data statistik dalam rangka evaluasi kegiatan kelembagaaan dalam bidang statistik: Lanjutan'),
        ('III.B.5.c.', 'III.B.5.c. Melakukan penyebarluasan hasil pengumpulan data statistik dalam rangka evaluasi kegiatan kelembagaaan dalam bidang statistik: Khusus'),
        ('III.B.6.', 'III.B.6. Membuat indikator statistik baru'),
        ('III.B.7.', 'III.B.7. Menyusun rencana induk (master plan) Sistem Statistik Nasional (SSN)'),
        ('III.B.8.', 'III.B.8. Melakukan revitalisasi rencana induk SSN sesuai kemajuan teknologi dan ilmu pengetahuan'),
        ('III.B.9.', 'III.B.9. Melakukan evaluasi SSN yang sedang berjalan'),
        ('III.B.10.', 'III.B.10. Melakukan kajian terhadap perkembangan dan pemanfaatan statistik secara internasional'),
        ('IV.A.1.a.', 'IV.A.1.a. Membuat karya tulis/ karya ilmiah hasil penelitian, pengkajian, survei, dan atau evaluasi di bidang statistik yang dipublikasikan dalam bentuk buku terbitan internasional'),
        ('IV.A.1.b.', 'IV.A.1.b. Membuat karya tulis/ karya ilmiah hasil penelitian, pengkajian, survei, dan atau evaluasi di bidang statistik yang dipublikasikan dalam bentuk buku yang diterbitkan dan diedarkan secara nasional'),
        ('IV.A.1.c.', 'IV.A.1.c. Membuat karya tulis/ karya ilmiah hasil penelitian, pengkajian, survei, dan atau evaluasi di bidang statistik yang dipublikasikan dalam bentuk majalah ilmiah yang diakui oleh LIPI'),
        ('IV.A.1.d.', 'IV.A.1.d. Membuat karya tulis/ karya ilmiah hasil penelitian, pengkajian, survei, dan atau evaluasi di bidang statistik yang dipublikasikan: karya tulis/ karya ilmiah diterbitkan lewat internet'),
        ('IV.A.2.a.', 'IV.A.2.a. Membuat karya tulis/ karya ilmiah hasil penelitian, pengkajian, survei, dan atau evaluasi di bidang statistik yang tidak dipublikasikan dalam bentuk buku'),
        ('IV.A.2.b.', 'IV.A.2.b. Membuat karya tulis/ karya ilmiah hasil penelitian, pengkajian, survei, dan atau evaluasi di bidang statistik yang tidak dipublikasikan dalam bentuk makalah'),
        ('IV.A.3.a.', 'IV.A.3.a. Membuat karya tulis/ karya ilmiah atau ulasan ilmiah hasil gagasan sendiri di bidang statistik yang dipublikasikan dalam bentuk buku yang diterbitkan dan diedarkan secara nasional'),
        ('IV.A.3.b.', 'IV.A.3.b. Membuat karya tulis/ karya ilmiah atau ulasan ilmiah hasil gagasan sendiri di bidang statistik yang dipublikasikan dalam majalah ilmiah yang diakui oleh LIPI'),
        ('IV.A.4.a.', 'IV.A.4.a. Membuat karya tulis/ karya ilmiah berupa tinjauan atau ulasan ilmiah hasil gagasan sendiri di bidang statistik yang tidak dipublikasikan dalam bentuk buku'),
        ('IV.A.4.b.', 'IV.A.4.b. Membuat karya tulis/ karya ilmiah berupa tinjauan atau ulasan ilmiah hasil gagasan sendiri di bidang statistik yang tidak dipublikasikan dalam bentuk makalah'),
        ('IV.A.5.', 'IV.A.5. Membuat karya tulis/ karya ilmiah populer di bidang statistik yang disebarluaskan melalui media massa'),
        ('IV.A.6.', 'IV.A.6. Membuat karya tulis/ karya ilmiah berupa tinjauan, atau ulasan ilmiah hasil gagasan sendiri di bidang statistik yang disampaikan dalam pertemuan ilmiah'),
        ('IV.B.', 'IV.B. Penyusunan petunjuk teknis pelaksanaan pengelolaan kegiatan statistik'),
        ('IV.C.1.a.', 'IV.C.1.a. Menerjemahkan / menyadur buku atau karya ilmiah dibidang statistik yang dipublikasikan: dalam bentuk buku yang diterbitkan dan diedarkan secara nasional'),
        ('IV.C.1.b.', 'IV.C.1.b. Menerjemahkan / menyadur buku atau karya ilmiah dibidang statistik yang dipublikasikan: dalam bentuk majalah ilmiah yang diakui oleh LIPI'),
        ('IV.C.2.a.', 'IV.C.2.a. Menerjemahkan / menyadur buku atau karya ilmiah dibidang statistik yang tidak dipublikasikan dalam bentuk buku'),
        ('IV.C.2.b.', 'IV.C.2.b. Menerjemahkan / menyadur buku atau karya ilmiah dibidang statistik yang tidak dipublikasikan dalam bentuk makalah'),
        ('IV.C.3..', 'IV.C.3. Membuat abstrak tulisan yang dimuat dalam majalah ilmiah'),
        ('V.A.1.', 'V.A.1. Memberikan bimbingan penuh kader statisti sampai mencapai tingkat doktor per orang, sebagai pembimbing pendamping'),
        ('V.A.2.a', 'V.A.2.a. Memberikan bimbingan penuh kader statisti sampai mencapai tingkat pascasarjana per orang, sebagai pembimbing utama'),
        ('V.A.2.b.', 'V.A.2.b. Memberikan bimbingan penuh kader statisti sampai mencapai tingkat pascasarjana per orang, sebagai pembimbing pendamping'),
        ('V.A.2.c.', 'V.A.2.c. Memberikan bimbingan penuh kader statisti sampai mencapai tingkat pascasarjana per orang, sebagai penguji'),
        ('V.A.3.a.', 'V.A.3.a. Memberikan bimbingan penuh kader statisti sampai mencapai tingkat sarjana / diploma IV per orang, sebagai pembimbing utama'),
        ('V.A.3.b.', 'V.A.3.b. Memberikan bimbingan penuh kader statisti sampai mencapai tingkat sarjana / diploma IV per orang, sebagai pembimbing pendamping'),
        ('V.A.4.', 'V.A.4. Memberikan bimbingan penuh kader statisti sampai mencapai tingkat diploma III per orang, sebagai pembimbing'),
        ('V.B.1.', 'V.B.1. Melaksanakan tugas mengajar pada kursus/ penataran statistik'),
        ('V.B.2.a.', 'V.B.2.a. Melaksanakan tugas mengajar pada perguruan tinggi, tiap SKS (maksimum 6 SKS), per semester: Strata 2 atau Strata 3'),
        ('V.B.2.b.', 'V.B.2.b. Melaksanakan tugas mengajar pada perguruan tinggi, tiap SKS (maksimum 6 SKS), per semester: Strata 1/ Diploma IV'),
        ('V.B.2.c.', 'V.B.2.c. Melaksanakan tugas mengajar pada perguruan tinggi, tiap SKS (maksimum 6 SKS), per semester: Diploma III'),
        ('V.C.1.', 'V.C.1. Mengikuti seminar/lokarya/konferensi sebagai: Pemrasaran'),
        ('V.C.2.', 'V.C.2. Mengikuti seminar/lokarya/konferensi sebagai: Moderator/pembahas/narasumber'),
        ('V.C.3.', 'V.C.3. Mengikuti seminar/lokarya/konferensi sebagai: Peserta'),
        ('V.D.', 'V.D. Menjadi anggota tim penilai jabatan fungsional statistisi'),
        ('V.E.1.a.', 'V.E.1.a. Menjadi anggota organisasi profesi pada tingkat nasional/ internasional sebagai: pengurus aktif'),
        ('V.E.1.b.', 'V.E.1.b. Menjadi anggota organisasi profesi pada tingkat nasional/ internasional sebagai: anggota aktif'),
        ('V.E.2.a.', 'V.E.2.a. Menjadi anggota organisasi profesi pada tingkat provinsi/ kabupaten/ kota sebagai: pengurus aktif'),
        ('V.E.2.b.', 'V.E.2.b. Menjadi anggota organisasi profesi pada tingkat provinsi/ kabupaten/ kota sebagai: anggota aktif'),
        ('V.F.1.a.', 'V.F.1.a. Memperoleh penghargaan/ tanda jasa satya lencana karya satya: 30 (tiga puluh) tahun'),
        ('V.F.1.b.', 'V.F.1.b. Memperoleh penghargaan/ tanda jasa satya lencana karya satya: 20 (dua puluh) tahun'),
        ('V.F.1.c.', 'V.F.1.c. Memperoleh penghargaan/ tanda jasa satya lencana karya satya: 10 (sepuluh) tahun'),
        ('V.F.2.', 'V.F.2. Gelar kehormatan akademis'),
        ('V.G.1.', 'V.G.1. Memperoleh gelar kesarjanaan yang tidak sesuai dengan bidang tugasnya: Doktor'),
        ('V.G.2.', 'V.G.2. Memperoleh gelar kesarjanaan yang tidak sesuai dengan bidang tugasnya: S2'),
        ('V.G.3.', 'V.G.3. Memperoleh gelar kesarjanaan yang tidak sesuai dengan bidang tugasnya: S1'),
        (None, '----- Bukan Kegiatan Statistisi -----'),
    ]

    UNSUR_PRANATA_KOMPUTER_CHOICES = [
        ('I.', 'I. Tata Kelola dan Tata Laksana Teknologi Informasi'),
        ('II.', 'II. Infrastruktur Teknologi Informasi'),
        ('III.', 'III. Sistem Informasi dan Multimedia'),
        (None, '----- Bukan Kegiatan Pranata Komputer -----'),
    ]

    SUB_UNSUR_PRANATA_KOMPUTER_CHOICES = [
        ('I.A.', 'I.A. IT Enterprise'),
        ('I.B.', 'I.B. Manajemen Layanan TI'),
        ('I.C.', 'I.C. Pengelolaan data (Data Management)'),
        ('I.D.', 'I.D. Audit TI'),
        ('I.E.', 'I.E. Manajemen risiko TI'),
        ('II.A.', 'II.A. Sistem Jaringan Komputer'),
        ('II.B.', 'II.B. Manajemen Infrastruktur TI'),
        ('III.A.', 'III.A. Sistem Informasi'),
        ('III.B.', 'III.B. Pengolahan Data'),
        ('III.C.', 'III.C. Area TI spesial / khusus'),
        (None, '----- Bukan Kegiatan Pranata Komputer -----'),
    ]

    BUTIR_KEGIATAN_PRANATA_KOMPUTER_CHOICES = [
        ('I.A.1.', 'I.A.1. Melakukan identifikasi dan analisis kebutuhan bisnis institusi'),
        ('I.A.2.', 'I.A.2. Melakukan reviu TI yang digunakan institusi saat ini atau tren TI terkini'),
        ('I.A.3.', 'I.A.3. Melakukan analisis terhadap strategi bisnis institusi yang berdampak pada strategi TI institusi'),
        ('I.A.4.', 'I.A.4. Melakukan analisis dampak TI yang digunakan institusi saat ini dan trennya terhadap perubahan strategi bisnis institusi'),
        ('I.A.5.', 'I.A.5. Menyusun kerangka kerja untuk penyusunan strategi TI'),
        ('I.A.6.', 'I.A.6. Melakukan pengkajian terhadap kerangka kerja untuk penyusunan strategi TI'),
        ('I.A.7.', 'I.A.7. Melakukan analisis kesenjangan terhadap strategi TI'),
        ('I.A.8.', 'I.A.8. Menyusun strategi TI'),
        ('I.A.9.', 'I.A.9. Melakukan pengkajian terhadap strategi TI'),
        ('I.A.10.', 'I.A.10. Menyusun komponen Enterprise Architecture (EA) saat ini'),
        ('I.A.11.', 'I.A.11. Menyusun pengembangan komponen Enterprise Architecture (EA) masa yang akan datang'),
        ('I.A.12.', 'I.A.12. Melakukan analisis kesenjangan terhadap komponen Enterprise Architecture (EA)'),
        ('I.A.13.', 'I.A.13. Melakukan pengkajian terhadap analisis kesenjangan terhadap komponen Enterprise Architecture (EA)'),
        ('I.A.14.', 'I.A.14. Membuat usulan roadmap pada masing-masing komponen Enterprise Architecture (EA)'),
        ('I.A.15.', 'I.A.15. Melakukan pengkajian terhadap usulan roadmap pada masing-masing komponen Enterprise Architecture (EA)'),
        ('I.A.16.', 'I.A.16. Menyusun strategi implementasi Enterprise Architecture (EA)'),
        ('I.A.17.', 'I.A.17. Melakukan pengkajian terhadap kelayakan strategi implementasi Enterprise Architecture (EA)'),
        ('I.A.18.', 'I.A.18. Menyusun atau mengkaji kerangka kerja tata kelola TI'),
        ('I.A.19.', 'I.A.19. Menyusun tata kelola TI'),
        ('I.A.20.', 'I.A.20. Melakukan pengkajian terhadap tata kelola TI'),
        ('I.A.21.', 'I.A.21. Menyusun struktur tata kelola TI'),
        ('I.A.22.', 'I.A.22. Menyusun atau mengkaji kerangka kerja kebijakan TI'),
        ('I.A.23.', 'I.A.23. Menyusun atau mengkaji kebijakan TI'),
        ('I.A.24.', 'I.A.24. Menyusun instrumen untuk mengukur keselarasan tujuan TI dan tujuan bisnis'),
        ('I.A.25.', 'I.A.25. Melakukan pengukuran dan pengkajian terhadap keselarasan tujuan TI dengan tujuan bisnis'),
        ('I.A.26.', 'I.A.26. Menetapkan target manfaat atau dampak dari implementasi TI'),
        ('I.A.27.', 'I.A.27. Melakukan evaluasi target manfaat atau dampak dari implementasi TI'),
        ('I.A.28.', 'I.A.28. Menetapkan cara mengukur performa TI'),
        ('I.A.29.', 'I.A.29. Melakukan pengukuran performa TI'),
        ('I.A.30.', 'I.A.30. Menyusun rencana TI'),
        ('I.A.31.', 'I.A.31. Menyusun revisi rencana TI'),
        ('I.A.32.', 'I.A.32. Menyusun skala prioritas solusi TI dalam Rencana TI'),
        ('I.A.33.', 'I.A.33. Menyusun rencana transformasi TI'),
        ('I.A.34.', 'I.A.34. Menyusun rencana pembiayaan TI'),
        ('I.A.35.', 'I.A.35. Menyusun templat/pola acu untuk strategi operasional rencana TI'),
        ('I.A.36.', 'I.A.36. Menyusun strategi operasional rencana TI'),
        ('I.A.37.', 'I.A.37. Melakukan pengkajian terhadap kelayakan implementasi rencana TI'),
        ('I.B.1.', 'I.B.1. Menyusun strategi layanan teknologi informasi'),
        ('I.B.2.', 'I.B.2. Mengelola kebutuhan layanan teknologi informasi'),
        ('I.B.3.', 'I.B.3. Menyusun portofolio layanan teknologi informasi'),
        ('I.B.4.', 'I.B.4. Mengelola portofolio layanan teknologi informasi'),
        ('I.B.5.', 'I.B.5. Mengelola anggaran layanan teknologi informasi'),
        ('I.B.6.', 'I.B.6. Menyusun SOP untuk kegiatan IT Service Management'),
        ('I.B.7.', 'I.B.7. Mengelola katalog layanan teknologi informasi'),
        ('I.B.8.', 'I.B.8. Mengelola penyedia jasa atau barang untuk layanan teknologi informasi'),
        ('I.B.9.', 'I.B.9. Mengelola kapasitas layanan teknologi informasi'),
        ('I.B.10.', 'I.B.10. Mengelola tingkat layanan teknologi informasi'),
        ('I.B.11.', 'I.B.11. Mengelola dukungan operasional layanan teknologi informasi'),
        ('I.B.12.', 'I.B.12. Melakukan pemantauan (monitoring) dan evaluasi ketersediaan layanan teknologi informasi'),
        ('I.B.13.', 'I.B.13. Menyusun perencanaan transisi layanan teknologi informasi'),
        ('I.B.14.', 'I.B.14. Mengelola perubahan layanan teknologi informasi'),
        ('I.B.15.', 'I.B.15. Mengelola aset dan konfigurasi layanan teknologi informasi'),
        ('I.B.16.', 'I.B.16. Mengelola pengetahuan layanan teknologi informasi'),
        ('I.B.17.', 'I.B.17. Melakukan validasi, pengujian, dan evaluasi layanan teknologi informasi'),
        ('I.B.18.', 'I.B.18. Mengelola rilis dan deployment layanan teknologi informasi'),
        ('I.B.19.', 'I.B.19. Mengelola event kegiatan teknologi informasi'),
        ('I.B.20.', 'I.B.20. Mengelola insiden kegiatan teknologi informasi'),
        ('I.B.21.', 'I.B.21. Mengelola permintaan dan layanan teknologi informasi'),
        ('I.C.1.', 'I.C.1. Menyusun atau mengelola strategi manajemen data instansi'),
        ('I.C.2.', 'I.C.2. Menyusun kebijakan data, standar data, atau prosedur pengelolaan data'),
        ('I.C.3.', 'I.C.3. Melakukan reviu kebijakan data, standar data, atau prosedur pengelolaan data'),
        ('I.C.4.', 'I.C.4. Menyusun rekomendasi persetujuan arsitektur data'),
        ('I.C.5.', 'I.C.5. Melakukan reviu rekomendasi persetujuan arsitektur data'),
        ('I.C.6.', 'I.C.6. Menyusun rencana kegiatan layanan pengelolaan data'),
        ('I.C.7.', 'I.C.7. Melakukan supervisi terhadap organisasi dan staf pengelola data'),
        ('I.C.8.', 'I.C.8. Menyusun alternatif solusi permasalahan pengelolaan data'),
        ('I.C.9.', 'I.C.9. Melakukan evaluasi pelaksanaan pengelolaan data'),
        ('I.C.10.', 'I.C.10. Menyusun bahan sosialisasi tentang pengelolaan data'),
        ('I.C.11.', 'I.C.11. Melakukan sosialisasi tentang pengelolaan data'),
        ('I.C.12.', 'I.C.12. Menyusun model data instansi'),
        ('I.C.13.', 'I.C.13. Melakukan analisis model data instansi'),
        ('I.C.14.', 'I.C.14. Menyusun arsitektur teknologi data'),
        ('I.C.15.', 'I.C.15. Menyusun arsitektur integrasi data'),
        ('I.C.16.', 'I.C.16. Melakukan perancangan data model'),
        ('I.C.17.', 'I.C.17. Melakukan implementasi data model'),
        ('I.C.18.', 'I.C.18. Melakukan perancangan business intelligence'),
        ('I.C.19.', 'I.C.19. Melakukan implementasi business intelligence'),
        ('I.C.20.', 'I.C.20. Menyusun taksonomi data'),
        ('I.C.21.', 'I.C.21. Menyusun arsitektur data'),
        ('I.C.22.', 'I.C.22. Menyusun standar metadata'),
        ('I.C.23.', 'I.C.23. Melakukan pengumpulan kebutuhan informasi'),
        ('I.C.24.', 'I.C.24. Melakukan analisis kebutuhan informasi'),
        ('I.C.25.', 'I.C.25. Melakukan perancangan layanan akses data'),
        ('I.C.26.', 'I.C.26. Melakukan implementasi rancangan layanan akses data'),
        ('I.C.27.', 'I.C.27. Menyusun prosedur pengujian rancangan layanan akses data'),
        ('I.C.28.', 'I.C.28. Melakukan perancangan integrasi data'),
        ('I.C.29.', 'I.C.29. Melakukan ingestion data'),
        ('I.C.30.', 'I.C.30. Melakukan implementasi rancangan integrasi data'),
        ('I.C.31.', 'I.C.31. Menyusun prosedur pengujian rancangan integrasi data'),
        ('I.C.32.', 'I.C.32. Melakukan evaluasi hasil pengujian rancangan integrasi data'),
        ('I.C.33.', 'I.C.33. Menyusun prosedur pengujian validasi kebutuhan informasi'),
        ('I.C.34.', 'I.C.34. Melakukan evaluasi hasil pengujian prosedur validasi kebutuhan informasi'),
        ('I.C.35.', 'I.C.35. Melakukan validasi kebutuhan informasi'),
        ('I.C.36.', 'I.C.36. Menyusun dokumentasi rancangan database'),
        ('I.C.37.', 'I.C.37. Melakukan instalasi dan konfigurasi DBMS'),
        ('I.C.38.', 'I.C.38. Menyusun rencana backup dan pemulihan data'),
        ('I.C.39.', 'I.C.39. Melakukan backup atau pemulihan data'),
        ('I.C.40.', 'I.C.40. Menyusun tingkat kinerja layanan database'),
        ('I.C.41.', 'I.C.41. Melakukan peningkatan kinerja database'),
        ('I.C.42.', 'I.C.42. Menyusun rencana retensi data'),
        ('I.C.43.', 'I.C.43. Menyusun kebutuhan teknologi data'),
        ('I.C.44.', 'I.C.44. Melakukan evaluasi teknologi data'),
        ('I.C.45.', 'I.C.45. Melakukan pengadministrasian teknologi data'),
        ('I.C.46.', 'I.C.46. Melakukan deteksi dan perbaikan terhadap permasalahan teknologi data'),
        ('I.C.47.', 'I.C.47. Melakukan implementasi data mining'),
        ('I.C.48.', 'I.C.48. Menyusun kebutuhan atau standar keamanan data'),
        ('I.C.49.', 'I.C.49. Menyusun kebijakan keamanan data'),
        ('I.C.50.', 'I.C.50. Menyusun definisi kontrol atau prosedur keamanan data'),
        ('I.C.51.', 'I.C.51. Mengelola pengguna dan hak akses data'),
        ('I.C.52.', 'I.C.52. Melakukan analisis perilaku akses pengguna'),
        ('I.C.53.', 'I.C.53. Menyusun pemetaan data berdasarkan tingkat kerahasiaan informasi'),
        ('I.D.1.', 'I.D.1. Melakukan studi kelayakan audit TI'),
        ('I.D.2.', 'I.D.2. Menyusun proposal audit TI'),
        ('I.D.3.', 'I.D.3. Melakukan perancangan proses bisnis dan SOP pelaksanaan audit TI'),
        ('I.D.4.', 'I.D.4. Melakukan pengkajian terhadap framework audit TI'),
        ('I.D.5.', 'I.D.5. Melakukan pengkajian terhadap tool dan aplikasi yang digunakan untuk audit TI'),
        ('I.D.6.', 'I.D.6. Melakukan analisis awal untuk kebutuhan audit TI'),
        ('I.D.7.', 'I.D.7. Melakukan pengumpulan data audit TI menggunakan metode tertentu'),
        ('I.D.8.', 'I.D.8. Melakukan pengujian, verifikasi, atau validasi terhadap data audit TI'),
        ('I.D.9.', 'I.D.9. Melakukan analisis data audit TI'),
        ('I.D.10.', 'I.D.10. Melakukan evaluasi kegiatan audit TI'),
        ('I.E.1.', 'I.E.1. Melakukan reviu dokumen manajemen risiko'),
        ('I.E.2.', 'I.E.2. Membuat framework manajemen risiko'),
        ('I.E.3.', 'I.E.3. Menyusun rencana manajemen risiko'),
        ('I.E.4.', 'I.E.4. Melakukan analisis faktor risiko'),
        ('I.E.5.', 'I.E.5. Melakukan identifikasi risiko'),
        ('I.E.6.', 'I.E.6. Melakukan pengukuran risiko'),
        ('I.E.7.', 'I.E.7. Menyusun strategi penanganan risiko'),
        ('I.E.8.', 'I.E.8. Membuat prosedur penanganan risiko'),
        ('I.E.9.', 'I.E.9. Menyusun solusi teknis penanganan risiko'),
        ('I.E.10.', 'I.E.10. Melakukan pemantauan (monitoring) terhadap strategi penanganan risiko'),
        ('I.E.11.', 'I.E.11. Melakukan evaluasi terhadap strategi penanganan risiko'),
        ('II.A.1.', 'II.A.1. Melakukan analisis kebutuhan pengguna sistem jaringan komputer kompleks'),
        ('II.A.2.', 'II.A.2. Melakukan analisis kondisi sistem jaringan komputer kompleks yang sedang berjalan'),
        ('II.A.3.', 'II.A.3. Membuat rancangan logis (logical design) sistem jaringan komputer'),
        ('II.A.4.', 'II.A.4. Membuat rancangan fisik (physical design) sistem jaringan komputer'),
        ('II.A.5.', 'II.A.5. Menerapkan rancangan fisik sistem jaringan komputer kompleks'),
        ('II.A.6.', 'II.A.6. Menerapkan rancangan logis sistem pengamanan jaringan komputer kompleks'),
        ('II.A.7.', 'II.A.7. Menyusun prosedur pemanfaatan sistem jaringan'),
        ('II.A.8.', 'II.A.8. Menyusun rancangan uji coba sistem jaringan kompleks'),
        ('II.A.9.', 'II.A.9. Melakukan uji coba sistem jaringan komputer kompleks'),
        ('II.A.10.', 'II.A.10. Melakukan evaluasi uji coba sistem jaringan komputer sederhana'),
        ('II.A.11.', 'II.A.11. Melakukan evaluasi uji coba sistem jaringan komputer kompleks'),
        ('II.A.12.', 'II.A.12. Menyusun dokumentasi penggunaan sistem jaringan komputer'),
        ('II.A.13.', 'II.A.13. Melakukan analisis permasalahan dari hasil pemantauan (monitoring) jaringan'),
        ('II.A.14.', 'II.A.14. Melakukan optimalisasi sistem jaringan'),
        ('II.A.15.', 'II.A.15. Melakukan deteksi dan atau perbaikan terhadap permasalahan yang terjadi pada sistem jaringan kompleks'),
        ('II.A.16.', 'II.A.16. Menyusun rumusan kebijakan keamanan jaringan'),
        ('II.A.17.', 'II.A.17. Melakukan reviu kebijakan keamanan jaringan'),
        ('II.A.18.', 'II.A.18. Menyusun prosedur keamanan jaringan'),
        ('II.A.19.', 'II.A.19. Menyusun petunjuk teknis sistem jaringan komputer dan keamanan jaringan'),
        ('II.A.20.', 'II.A.20. Melakukan pemeriksaan kepatuhan terhadap kebijakan keamanan jaringan'),
        ('II.B.1.', 'II.B.1. Menyusun rencana pengoperasian infrastruktur TI'),
        ('II.B.2.', 'II.B.2. Menyusun KAK'),
        ('II.B.3.', 'II.B.3. Melakukan evaluasi proposal teknis penyedia barang/jasa infrastruktur TI'),
        ('II.B.4.', 'II.B.4. Melakukan pengkajian terhadap pemenuhan/ kesesuaian infrastruktur TI terhadap regulasi'),
        ('II.B.5.', 'II.B.5. Melakukan pemeriksaan kesesuaian antara Infrastruktur TI dengan spesifikasi teknis'),
        ('II.B.6.', 'II.B.6. Melakukan pengujian infrastruktur TI'),
        ('II.B.7.', 'II.B.7. Menyusun rencana pemeliharaan infrastruktur TI'),
        ('II.B.8.', 'II.B.8. Melakukan pemeliharaan infrastruktur TI'),
        ('II.B.9.', 'II.B.9. Melakukan pemasangan infrastruktur TI'),
        ('II.B.10.', 'II.B.10. Melakukan pengaturan akses keamanan fisik TI'),
        ('II.B.11.', 'II.B.11. Melakukan analisis permasalahan dari hasil pemantauan (monitoring) kinerja infrastruktur TI'),
        ('II.B.12.', 'II.B.12. Melakukan deteksi dan atau perbaikan terhadap permasalahan infrastruktur TI'),
        ('II.B.13.', 'II.B.13. Menyusun prosedur pemanfaatan infrastruktur TI'),
        ('II.B.14.', 'II.B.14. Menyiapkan peralatan video conference (vicon/streaming), monitoring peralatan (audio, video, dan perangkat jaringan), dan mengatur layout'),
        ('II.B.15.', 'II.B.15. Melakukan optimalisasi kinerja infrastruktur TI'),
        ('III.A.1.', 'III.A.1. Menyusun usulan pembangunan sistem informasi'),
        ('III.A.2.', 'III.A.2. Menyusun rencana studi kelayakan sistem informasi'),
        ('III.A.3.', 'III.A.3. Melakukan studi kelayakan sistem informasi'),
        ('III.A.4.', 'III.A.4. Melakukan identifikasi kebutuhan pengguna sistem informasi'),
        ('III.A.5.', 'III.A.5. Melakukan analisis sistem informasi'),
        ('III.A.6.', 'III.A.6. Melakukan pemodelan proses sistem informasi'),
        ('III.A.7.', 'III.A.7. Melakukan perancangan sistem informasi'),
        ('III.A.8.', 'III.A.8. Membuat algoritma pemrograman'),
        ('III.A.9.', 'III.A.9. Membuat program aplikasi / sistem informasi'),
        ('III.A.10.', 'III.A.10. Mengembangkan program aplikasi sistem informasi'),
        ('III.A.11.', 'III.A.11. Menyusun definisi rule validasi pada program aplikasi sistem informasi'),
        ('III.A.12.', 'III.A.12. Melakukan penyiapan data untuk uji coba sistem informasi'),
        ('III.A.13.', 'III.A.13. Menyusun skenario uji coba sistem informasi'),
        ('III.A.14.', 'III.A.14. Melakukan uji coba sistem informasi'),
        ('III.A.15.', 'III.A.15. Melakukan pemeriksaan dan analisis hasil uji coba sistem informasi'),
        ('III.A.16.', 'III.A.16. Melakukan deteksi dan atau perbaikan kerusakan sistem informasi'),
        ('III.A.17.', 'III.A.17. Menyusun petunjuk operasional  program  aplikasi sistem informasi'),
        ('III.A.18.', 'III.A.18. Menyusun dokumentasi pengembangan sistem informasi'),
        ('III.A.19.', 'III.A.19. Melakukan instalasi/upgrade dan konfigurasi sistem operasi/aplikasi'),
        ('III.A.20.', 'III.A.20. Melakukan pemantauan (monitoring) kinerja aplikasi sistem informasi di lingkungan instansi'),
        ('III.B.1.', 'III.B.1. Menyusun rencana studi kelayakan untuk pengolahan data'),
        ('III.B.2.', 'III.B.2. Melakukan studi kelayakan untuk pengolahan data'),
        ('III.B.3.', 'III.B.3. Menyusun prosedur pengolahan data'),
        ('III.B.4.', 'III.B.4. Menyusun petunjuk teknis pelaksanaan pengolahan data'),
        ('III.B.5.', 'III.B.5. Melakukan  data crawling, data feeding, atau data loading'),
        ('III.B.6.', 'III.B.6. Melakukan manipulasi data'),
        ('III.B.7.', 'III.B.7. Melakukan pemantauan (monitoring) pengolahan data'),
        ('III.B.8.', 'III.B.8. Melakukan evaluasi pengolahan data'),
        ('III.C.1.', 'III.C.1. Menyusun definisi sistem proyeksi pada suatu data spasial'),
        ('III.C.2.', 'III.C.2. Membuat peta tematik rinci'),
        ('III.C.3.', 'III.C.3. Melakukan pengolahan data atribut dan spasial rinci'),
        ('III.C.4.', 'III.C.4. Melakukan analisis data spasial'),
        ('III.C.5.', 'III.C.5. Mengoperasikan tools untuk membuat storyboard'),
        ('III.C.6.', 'III.C.6. Membuat flowchart untuk pemrograman multimedia'),
        ('III.C.7.', 'III.C.7. Melakukan editing objek multimedia kompleks dengan piranti lunak'),
        ('III.C.8.', 'III.C.8. Membuat objek multimedia kompleks dengan piranti lunak'),
        ('III.C.9.', 'III.C.9. Membuat prototype kompleks pada program multimedia'),
        ('III.C.10.', 'III.C.10. Membuat program multimedia kompleks'),
        ('III.C.11.', 'III.C.11. Menyusun skenario uji coba program multimedia'),
        (None, '----- Bukan Kegiatan Pranata Komputer -----'),
    ]

    jenis_fungsional = models.CharField(
        max_length=30,
        choices=JENIS_FUNGSIONAL_CHOICES,
        blank=True,
    )

    unsur_statistisi = models.CharField(
        max_length=50,
        choices=UNSUR_STATISTISI_CHOICES,
        blank=True,
    )

    sub_unsur_statistisi = models.CharField(
        max_length=150,
        choices=SUB_UNSUR_STATISTISI_CHOICES,
        blank=True,
    )

    butir_kegiatan_statistisi = models.CharField(
        max_length=255,
        choices=BUTIR_KEGIATAN_STATISTISI_CHOICES,
        blank=True,
    )

    unsur_pranata_komputer = models.CharField(
        max_length=70,
        choices=UNSUR_PRANATA_KOMPUTER_CHOICES,
        blank=True,
    )

    sub_unsur_pranata_komputer = models.CharField(
        max_length=60,
        choices=SUB_UNSUR_PRANATA_KOMPUTER_CHOICES,
        blank=True,
    )

    butir_kegiatan_pranata_komputer = models.CharField(
        max_length=180,
        choices=BUTIR_KEGIATAN_PRANATA_KOMPUTER_CHOICES,
        blank=True,
    )

    # Memakai float
    angka_kredit = models.FloatField()

    PELAKSANA_KEGIATAN_CHOICES = [
        ('1', 'Pertama'),
        ('2', 'Muda'),
        ('3', 'Madya'),
        ('4', 'Utama'),
        ('5', 'Semua Jenjang'),
        (None, '----- Bukan Kegiatan Fungsional -----'),
    ]

    pelaksana_kegiatan = models.CharField(
        max_length=30,
        choices=PELAKSANA_KEGIATAN_CHOICES,
        blank=True,
    )

    def __str__(self):
        if self.jenis_fungsional == 'ST':
            return self.jenis_fungsional + " " + self.butir_kegiatan_statistisi
        elif self.jenis_fungsional == 'PR':
            return self.jenis_fungsional + " " + self.butir_kegiatan_pranata_komputer
        else:
            return "Bukan Kegiatan Fungsional " + str(self.angka_kredit)

# Kelas untuk menyimpan kegiatan yang akan dipakai di ckp
class MasterKegiatan(models.Model):
    uraian_kegiatan = models.TextField()

    subject_matter = models.CharField(
        max_length=80,
        choices=CustomUser.JABATAN_KANTOR_CHOICES,
        default='7',
    )

    butir_kegiatan = models.ForeignKey(MasterButirKegiatan, on_delete=SET_NULL, null=True, blank=True)

    satuan = models.CharField(
        max_length=60,
    )

    author = models.ForeignKey(
        CustomUser, on_delete=models.DO_NOTHING, default=1)

    def get_subject_matter_singkat(self):
        singkat = self.get_subject_matter_display()
        if singkat == 'Koordinator Fungsi Integrasi Pengolahan dan Diseminasi Statistik':
            return 'IPDS'
        elif singkat == 'Koordinator Fungsi Neraca Wilayah dan Analisis Statistik':
            return 'Neraca Wilayah dan Analisis Statistik'
        else:
            return " ".join(singkat.split()[2:])

    def __str__(self):
        return self.uraian_kegiatan
        # return self.butir_kegiatan.__str__()

class DokumenCKP(models.Model):
    pegawai = models.ForeignKey(CustomUser, on_delete=CASCADE)
    periode = models.DateTimeField(null=True)

    def get_daftar_bulan_max():
        sekarang= datetime.now()
        awal_tahun = datetime(sekarang.year, 1, 1)
        bulan_terakhir = datetime.now() + relativedelta(months=1) # range bulan, dari bulan sekarang + 1
        locale.setlocale(locale.LC_TIME, "IND")
        return [(awal_tahun + relativedelta(months=i)).strftime("%B") for i in range(bulan_terakhir.month)]
    
    def get_status_penilaian(self):
        butir_ckp_set = self.butirckp_set.all()
        lengkap = True
        
        if len(butir_ckp_set) == 0:
            lengkap = False

        for butir_ckp in butir_ckp_set:
            if butir_ckp.realisasi is None or butir_ckp.tingkat_kualitas is None:
                lengkap = False
        
        return lengkap
    
    def __str__(self):
        return str(self.id) + ' CKP ' + self.pegawai.get_full_name() + ' ---- ' + self.periode.strftime("%d %B, %Y")

class ButirCKP(models.Model):

    JENIS_BUTIR_CKP_CHOICES = [
        ('UTAMA', 'Utama'),
        ('TAMBAHAN', 'Tambahan')
    ]

    dokumen_ckp = models.ManyToManyField(DokumenCKP)

    jenis_butir_ckp = models.CharField(
        max_length=10,
        choices=JENIS_BUTIR_CKP_CHOICES,
    )
    
    kegiatan = models.ForeignKey(MasterKegiatan, on_delete=CASCADE)
    target = models.IntegerField()
    realisasi = models.IntegerField(blank=True, null=True)
    tingkat_kualitas = models.FloatField(blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)

class PIA(models.Model):
    pegawai_dinilai = models.ForeignKey(CustomUser, on_delete=CASCADE, related_name="pegawai_dinilai")
    pegawai_penilai = models.ForeignKey(CustomUser, on_delete=CASCADE,related_name="pegawai_penilai")
    periode = models.DateTimeField(null=True)

    profesional = models.FloatField(null=True)
    integritas = models.FloatField(null=True)
    amanah = models.FloatField(null=True)

    total = models.FloatField(null=True, default=0)

    def __str__(self):
        return str(self.id) + ' PIA ' + self.pegawai_penilai.get_full_name() + ' ---- ' + self.pegawai_dinilai.get_full_name() + ' ---- ' + self.periode.strftime("%d %B, %Y")

class PIAAgregat(models.Model):
    pegawai = models.ForeignKey(CustomUser, on_delete=CASCADE)
    periode = models.DateTimeField(null=True)
    PIA = models.FloatField(null=True, default=0)

    def __str__(self):
        return str(self.id) + ' Agregat PIA ' + self.pegawai.get_full_name() + ' ---- ' + self.periode.strftime("%d %B, %Y")