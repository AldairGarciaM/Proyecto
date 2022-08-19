# Generated by Django 4.0.5 on 2022-08-17 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0006_perfil_compras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
