from email import message
from importlib.resources import contents
from multiprocessing import context
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from .models import Cursos
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import userRegisterForm

# Create your views here.

def cursos(request):
    cursos= Cursos.objects.all()

    return render(request, "principal/cursos.html", {"cursos": cursos})

def registro(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado correctamente')
            return redirect('Login')
    else:
        form= userRegisterForm()
        
    context= {'form': form}

    return render(request, "registration/registro.html", context)

def categorias(request):
    return render(request, "principal/categorias.html")

def home(request):
    return render(request, 'principal/home.html')

def infoCursos(request,id):
    cursos= Cursos.objects.get(id=id)
    return render(request, 'principal/infoCurso.html', {'cursos': cursos})

def misCursos(request):
    return render(request, 'principal/misCursos.html')

def cursoProgra(request):
    cursos= Cursos.objects.filter(categoria="Programacion")

    return render(request, 'principal/cursos.html', {"cursos":cursos})

def cursoAnima(request):
    cursos= Cursos.objects.filter(categoria="Animacion Digital")

    return render(request, 'principal/cursos.html', {"cursos":cursos})