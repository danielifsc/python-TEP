from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Avaliacao


class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',   
            }),

            'email': forms.TextInput(attrs={
                'class': 'form-control',   
            }),
        }

class AvaliacaoForm(forms.ModelForm):
    
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario']
        widgets = {
            'nota': forms.RadioSelect(attrs={'class': 'rating-input'}),
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4, 
                'placeholder': 'Compartilhe a sua experiência...'})
        }