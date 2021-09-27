from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class meta:
        model = CustomUser
        fields = "__all__"


class CustomUserChangeForm(UserChangeForm):

    class meta:
        model = CustomUser
        fields = "__all__"

class CustomeUserUpdateProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name', 'email', 'no_hp', 'foto_profil']