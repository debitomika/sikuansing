from django.contrib import admin
from .models import ButirCKP, DokumenCKP, MasterKegiatan, MasterButirKegiatan, PIA, PIAAgregat

class MasterButirKegiatanAdmin(admin.ModelAdmin):
    model = MasterButirKegiatan
    list_display = ('jenis_fungsional', 'butir_kegiatan_statistisi', 'butir_kegiatan_pranata_komputer', 'angka_kredit')

admin.site.register(MasterKegiatan)
admin.site.register(MasterButirKegiatan, MasterButirKegiatanAdmin)
admin.site.register(DokumenCKP)
admin.site.register(ButirCKP)
admin.site.register(PIA)
admin.site.register(PIAAgregat)