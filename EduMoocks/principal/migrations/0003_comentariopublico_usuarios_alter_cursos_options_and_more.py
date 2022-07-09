# Generated by Django 4.0.5 on 2022-07-08 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_alter_cursos_options_cursos_creates_cursos_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioPublico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Llave')),
                ('usuario', models.CharField(max_length=50, verbose_name='Usuario')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
            ],
            options={
                'verbose_name': 'Comentario Publico',
                'verbose_name_plural': 'Comentarios Publicos',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('correo', models.CharField(max_length=50, verbose_name='Email')),
                ('contraseña', models.CharField(max_length=50, verbose_name='Password')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
                ('update', models.DateTimeField(auto_now_add=True, verbose_name='Actualizacion')),
            ],
            options={
                'verbose_name': 'Usuarios',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.AlterModelOptions(
            name='cursos',
            options={'ordering': ['-creates'], 'verbose_name': 'Cursos', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Numero')),
                ('mensaje', models.TextField(verbose_name='Comentario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.usuarios', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
    ]
