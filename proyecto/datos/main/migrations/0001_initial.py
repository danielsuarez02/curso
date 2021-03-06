# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 15:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('dir', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.CharField(max_length=140)),
                ('genero', models.CharField(max_length=140)),
                ('titulo', models.CharField(max_length=140)),
                ('cines', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peliculas', to='main.Cine')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('tel', models.CharField(max_length=13)),
                ('genero', models.CharField(choices=[(b'hombre', b'HOMBRE'), (b'mujer', b'MUJER')], max_length=6)),
                ('alias', models.CharField(max_length=10)),
                ('domicilio', models.TextField()),
                ('ocupacion', models.CharField(choices=[(b'estudiante', b'ESTUDIANTE'), (b'academico', b'ACADEMICO'), (b'publico', b'PUBLICO'), (b'empresa', b'EMPRESA'), (b'godinez', b'GODINEZ')], max_length=140)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('desc', models.TextField()),
                ('precio', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
