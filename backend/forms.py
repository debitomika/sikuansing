from backend.models import ButirCKP, MasterKegiatan, DokumenCKP
from django import forms


class KegiatanCreationForm(forms.ModelForm):

    class Meta:
        model = MasterKegiatan
        fields = ['uraian_kegiatan', 'butir_kegiatan', 'satuan']

class AdminKegiatanCreationForm(forms.ModelForm):

    class Meta:
        model = MasterKegiatan
        fields = "__all__"

class DokumenCKPCreationForm(forms.ModelForm):

    class Meta:
        model = DokumenCKP
        fields =  ['pegawai']

class ButirCKPCreationFormR(forms.ModelForm):

    class Meta:
        model = ButirCKP
        fields = ['jenis_butir_ckp', 'target', 'keterangan']

class PenilaianButirCKPForm(forms.ModelForm):

    class Meta:
        model = ButirCKP
        fields = ['tingkat_kualitas','realisasi','keterangan']