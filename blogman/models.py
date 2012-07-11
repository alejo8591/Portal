# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Category(models.Model):
    b_title = models.CharField(max_length=250, verbose_name='Título', help_text="Título de la Categoria, max. 250 caracteres")
    b_slug = models.SlugField(unique=True, verbose_name='Slug', help_text="Direcciónes para el trabajo SEO")
    b_description = models.TextField(verbose_name='Descripción', help_text="Descripción del articulo")
    
    class Meta:
        ordering = ['b_title']
        verbose_name_plural = "Categories"
        
    def get_absolute_url(self):
        return "/categories/%s/" % self.b_slug
    
    def __unicode__(self):
        return b_title
    
class Entry(models.Model):
    e_author = models.ForeignKey(User)
    e_title = models.CharField(max_length=250, verbose_name='Título', help_text="Título del Post, max. 250 caracteres")
    e_excerpt = models.TextField(blank=True, verbose_name='Resumen', help_text="Resumen del Post")
    e_body = models.TextField(verbose_name='Body', help_text="Cuerpo del Post")
    e_pub_date = models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de Publicación', help_text="Fecha de Publicación del Post")
    e_slug = models.SlugField(unique_for_date = 'e_pub_date', verbose_name='Slug', help_text="Direcciónes para el trabajo SEO")
    
    
    def __unicode__(self):
        return e_title