from django.contrib import admin
from .models import Cursos, Usuarios, Comentarios, ComentarioPublico, Ventas

# Register your models here.

class ModeloCursos(admin.ModelAdmin):
    readonly_fields= ('creates', 'update')
    list_display= ('nombre', 'categoria', 'creador', 'precio')
    search_fields= ('nombre', 'categoria', 'creador')
    date_hierarchy= 'creates'
    list_filter= ('categoria', 'creador')

admin.site.register(Cursos,ModeloCursos)

admin.site.register(Usuarios)

admin.site.register(Comentarios)

admin.site.register(ComentarioPublico)

admin.site.register(Ventas)