"""EduMoocks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from contenido import views
from django.conf import settings
from principal import views as views_principal
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="Principal"),
    path('contacto/', views_principal.Comentario, name="Comentario"),
    path('ListaCursos/', views.listaCurso, name="Lista"),
    path('cursos/', views_principal.cursos, name="Cursos"),
    path('registro/', views_principal.registro, name="Registro"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name="Login"),
    path('logout/', LogoutView.as_view(template_name='registration/login.html'), name="Logout"),
    path('categorias/', views_principal.categorias, name="Categorias"),
    path('home/', views_principal.home, name="Principal"),
    path('InfoCursos/<int:id>/', views_principal.infoCursos, name="Informacion"),
    path('comprar/<int:id>/', views_principal.Comprar, name="Comprar"),
    path('MisCursos/<int:id>/', views_principal.misCursos, name="MisCursos"),
    path('programacion/', views_principal.cursoProgra, name="Programacion"),
    path('animacion/', views_principal.cursoAnima, name="Animacion"),
    path('seguridad/', views_principal.cursoSeguridad, name="Seguridad"),
    path('robotica/', views_principal.cursoRobo, name="Robotica"),
    path('bases/', views_principal.cursoBases, name="Bases"),
    path('servidores/', views_principal.cursoServi, name="Servidores"),

]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)