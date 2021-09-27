from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.models import CustomUser
from .forms import CustomeUserUpdateProfileForm
from django.contrib import messages


@login_required
def profil(request):
    return render(request, 'accounts/profil.html')

# 'first_name','last_name', 'email', 'no_hp', 'foto_profil'
@login_required
def edit_profil(request, pk):
    user = CustomUser.objects.get(id=pk)

    if request.method == 'POST':
        form = CustomeUserUpdateProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.username = user.username
            fs.password = user.password
            fs.is_staff = user.is_staff
            fs.is_active = user.is_active
            fs.is_superuser = user.is_superuser
            fs.last_login = user.last_login
            fs.date_joined = user.date_joined
            fs.nip = user.nip
            fs.nip_lama = user.nip_lama
            fs.no_hp = user.no_hp
            fs.pangkat_golongan = user.pangkat_golongan
            fs.jabatan_kantor = user.jabatan_kantor
            fs.jabatan_fungsional = user.jabatan_fungsional
            fs.save()
            messages.success(
                request, f'SUKSES! Profil berhasil diupdate')
            return redirect('profil')
        else:
            print()
            form = CustomeUserUpdateProfileForm()

    context = {
        'user': user,
        'title': 'Edit Profil '+ user.get_full_name(),
    }

    return render(request, 'accounts/editprofil.html', context)