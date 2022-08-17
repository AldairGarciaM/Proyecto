from django.contrib import admin
from .models import Cursos, Usuarios, Comentarios, ComentarioPublico, Ventas
from django.contrib.auth.models import User

# Register your models here.

class ModeloCursos(admin.ModelAdmin):
    readonly_fields= ('creates', 'update')
    list_display= ('id','nombre', 'categoria', 'creador', 'precio')
    search_fields= ('nombre', 'categoria', 'creador')
    date_hierarchy= 'creates'
    list_filter= ('categoria', 'creador')

class User(admin.ModelAdmin):
    readonly_fields= ('creates', 'update')
    list_display= ('id','username', 'email')
   

admin.site.register(Cursos,ModeloCursos)

admin.site.register(Usuarios)

admin.site.register(Comentarios)

admin.site.register(ComentarioPublico)

admin.site.register(Ventas)
