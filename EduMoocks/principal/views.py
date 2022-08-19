from email import message
from importlib.resources import contents
from multiprocessing import context
from sre_constants import SUCCESS
from tracemalloc import get_object_traceback
from django.shortcuts import render, redirect
from .models import Cursos, compras, Comentarios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import userRegisterForm, compraCurso, ComentarioContactoForm
from django.shortcuts import get_object_or_404

# Create your views here.

def cursos(request):
    cursos= Cursos.objects.all()

    return render(request, "principal/cursos.html", {"cursos": cursos})


def Comentario(request):
    comentario= Comentarios.objects.all()
    if request.method == 'POST':
        form= ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Comentario')

    form= ComentarioContactoForm()
    return render(request, "principal/Contacto.html", {'comentario': comentario})


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


def Comprar(request, id):
    Curso= Cursos.objects.get(id=id)
    if request.method == 'POST':
        form= compraCurso(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "principal/categorias.html",{'Curso': Curso, 'form': form})
    form= compraCurso()
    return render(request, "principal/comprarCurso.html",{'Curso': Curso, 'form': form})
    


def misCursos(request,id):
    user=User.objects.get(id=id)
    comprado=compras.objects.filter(user=user.id)
    Compras= compras.objects.all()
    return render(request, 'principal/misCursos.html', {'Compras': Compras, 'comprado': comprado,'user':user})



def cursoProgra(request):
    cursos= Cursos.objects.filter(categoria="Programacion")
    return render(request, 'principal/cursos.html', {"cursos":cursos})


def cursoAnima(request):
    cursos= Cursos.objects.filter(categoria="Animacion Digital")
    return render(request, 'principal/cursos.html', {"cursos":cursos})


def cursoSeguridad(request):
    cursos= Cursos.objects.filter(categoria="Seguridad Web")
    return render(request, 'principal/cursos.html', {"cursos":cursos})


def cursoRobo(request):
    cursos= Cursos.objects.filter(categoria="Robotica")
    return render(request, 'principal/cursos.html', {"cursos":cursos})


def cursoBases(request):
    cursos= Cursos.objects.filter(categoria="Bases de datos")
    return render(request, 'principal/cursos.html', {"cursos":cursos})

def cursoServi(request):
    cursos= Cursos.objects.filter(categoria="Desarrollo de Servidores")
    return render(request, 'principal/cursos.html', {"cursos":cursos})