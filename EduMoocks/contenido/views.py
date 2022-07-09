from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "contenido/inicio.html")

def contacto(request):
    return render(request, "contenido/contacto.html")

def cursos(request):
    return render(request, "contenido/cursos.html")