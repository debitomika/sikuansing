from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='backend-home'),
    # URL Kegiatan
    path('masterkegiatan/', views.masterkegiatan, name='sicakep-masterkegiatan'),
    path('tambahkegiatan/', views.tambah_kegiatan,
         name='sicakep-tambahkegiatan'),
    path('detailkegiatan/<int:pk>/', views.detail_kegiatan,
         name='sicakep-detailkegiatan'),
    path('updatekegiatan/<int:pk>/', views.update_kegiatan,
         name='sicakep-updatekegiatan'),
    path('deletekegiatan/<int:pk>/', views.delete_kegiatan,
         name='sicakep-deletekegiatan'),
    path('tambahckppegawai/', views.tambah_ckp_pegawai,
         name='sicakep-tambahckppegawai'),
    # URL CKP
    path('daftarckp/', views.daftar_ckp, name='sicakep-daftarckp'),
    path('detailckp/<int:pk>/', views.detail_ckp, name='sicakep-detailckp'),
    path('tambahkegiatanckp/<int:pk>/', views.tambah_kegiatan_ckp, name='sicakep-tambahkegiatanckp'),
    path('delete_dokumen_ckp/<int:pk>/', views.delete_dokumen_ckp, name='sicakep-deletedokumenckp'),
    path('delete_butir_ckp/<int:btpk>/<int:dkpk>/', views.delete_butir_ckp, name='sicakep-deletebutirckp'),
    path('penilaianckp/<int:pk>/', views.penilaian_ckp, name='sicakep-penilaianckp'),
    path('export-excel/<int:pk>/', views.export_xls_ckp, name='sicakep-export-excel'),
    
    # URL PIA
    path('daftarpenilaianpia/', views.daftar_penilaian_pia, name='sipia-daftar-penilaian-pia'),
    path('penilaianpia/<int:pk>/', views.penilaian_pia, name='sipia-penilaianpia'),
    path('hasilpenilaianpia/', views.hasil_penilaian_pia, name='sipia-hasil-penilaian-pia'),
    
    # URL Ajax
    path('ajax/load-satuan/', views.load_satuan, name='ajax_load_satuan'),
    path('ajax/load-butir-kegiatan/', views.load_butir_kegiatan, name='ajax_load_butir_kegiatan'),
    path('ajax/load-angka-kredit/', views.load_angka_kredit, name='ajax_load_angka_kredit'),
    path('ajax/load-master-angka-kredit/', views.load_master_angka_kredit, name='ajax_load_master_angka_kredit'),
]
