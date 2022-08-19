from distutils.command.upload import upload
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cursos(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="ID")
    nombre= models.CharField(max_length=50, verbose_name="Nombre")
    categoria= models.CharField(max_length=50, verbose_name="Categoria")
    creador= models.CharField(max_length=50, verbose_name="Profesor")
    descripcion= models.TextField(verbose_name="Descripcion")
    contenido= models.TextField(verbose_name="Contenido")
    precio= models.CharField(max_length=50, verbose_name="Precio")
    imagen= models.ImageField(null=True, upload_to="imagenes", verbose_name="Imagenes")
    creates= models.DateTimeField(auto_now_add=True, verbose_name="Creacion")
    update= models.DateField(auto_now_add=True, verbose_name="Actualizacion")

    class Meta:
        verbose_name= "Cursos"
        verbose_name_plural= "Cursos"
        ordering= ["-creates"]

    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="Id")
    nombre= models.CharField(max_length=50, verbose_name="Nombre")
    correo= models.CharField(max_length=50, verbose_name="Email")
    contraseña= models.CharField(max_length=50, verbose_name="Password")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Creacion")
    update= models.DateTimeField(auto_now_add=True, verbose_name="Actualizacion")

    class Meta:
        verbose_name="Usuarios"
        verbose_name_plural= "Usuarios"

    
    def __str__(self):
        return self.nombre

class Comentarios(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="Numero")
    nombre= models.CharField(max_length=255, verbose_name="Usuario")
    mensaje= models.TextField(verbose_name="Comentario")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Creacion")

    class Meta:
        verbose_name= "Comentario"
        verbose_name_plural= "Comentarios"
        ordering=["-created"]

    def __str__(self):
        return self.nombre


class ComentarioPublico(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="Llave")
    usuario= models.CharField(max_length=50, verbose_name="Usuario")
    mensaje= models.TextField(verbose_name="Mensaje")
    creacion= models.DateTimeField(auto_now_add=True, verbose_name="Creacion")

    class Meta:
        verbose_name="Comentario Publico"
        verbose_name_plural= "Comentarios Publicos"

    def __str__(self):
        return self.usuario

class perfil(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="ID")
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'Cuenta de {self.user.username}'


class compras(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="compras")
    curso= models.CharField(max_length=50, verbose_name="Curso")
    precio= models.CharField(max_length=50, verbose_name="Costo")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    class Meta:
        verbose_name="Compra"
        verbose_name_plural= "Compras"
        ordering=["-created"]

    def __str__(self):
        return f'{self.user.username}: {self.curso}: {self.precio}'
