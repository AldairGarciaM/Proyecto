# Generated by Django 4.0.5 on 2022-08-17 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_ventas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='Usuario'),
        ),
        migrations.DeleteModel(
            name='Ventas',
        ),
    ]
