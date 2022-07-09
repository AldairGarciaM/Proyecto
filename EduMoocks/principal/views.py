from django.shortcuts import render
from .models import Cursos

# Create your views here.

def cursos(request):
    cursos= Cursos.objects.all()

    return render(request, "principal/cursos.html", {"cursos": cursos})

def registro(request):
    return render(request, "principal/registro.html")

def login(request):
    return render(request, "principal/login.html")

def categorias(request):
    return render(request, "principal/categorias.html")