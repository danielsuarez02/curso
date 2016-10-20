# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='nombre',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='contenido',
        ),
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='categorias',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
