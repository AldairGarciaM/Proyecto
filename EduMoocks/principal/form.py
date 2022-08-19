from dataclasses import field, fields
from django import forms
from .models import compras, Comentarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class userRegisterForm(UserCreationForm):
    username= forms.CharField(max_length="100", label="Nombre de usuario")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        help_text= {k:"" for k in fields}

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model= Comentarios
        fields=['nombre', 'mensaje']

class compraCurso(forms.ModelForm):
    class Meta:
        model= compras
        fields= ['user', 'curso', 'precio']