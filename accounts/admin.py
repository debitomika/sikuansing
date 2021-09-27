from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nip', 'nip_lama', 'no_hp',
                           'pangkat_golongan', 'jabatan_kantor', 'jabatan_fungsional', 'foto_profil')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
