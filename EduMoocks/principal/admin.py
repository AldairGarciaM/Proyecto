from django.contrib import admin
from .models import Cursos, Comentarios, ComentarioPublico, perfil, compras
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
   
class Perfil(admin.ModelAdmin):
    list_display= ('id', 'user')

admin.site.register(Cursos,ModeloCursos)

admin.site.register(Comentarios)

admin.site.register(ComentarioPublico)

admin.site.register(perfil, Perfil)

admin.site.register(compras)


