from django.forms import forms
from django.forms import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Usuarioform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
                  'username': forms.TextInput(attrs={
                  'class':'form-control',
        }),
    }