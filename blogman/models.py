# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# ----- tagging in test
#from tagging.fields import TagField
from taggit.managers import TaggableManager
from markdown import markdown

class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Título', help_text="Título de la Categoria, max. 250 caracteres")
    slug = models.SlugField(unique=True, verbose_name='Slug', help_text="Direcciónes para el trabajo SEO")
    description = models.TextField(verbose_name='Descripción', help_text="Descripción del articulo")
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"
        
    def get_absolute_url(self):
        return "/categories/%s/" % self.slug
    
    def __unicode__(self):
        return self.title
    
class Entry(models.Model):
    STATUS_CHOICES = (
        (1, 'Live'),
        (2, 'Draft'),
        (3, 'Hidden'),
    )
    author = models.ForeignKey(User, verbose_name='Autor', help_text="Nombre del Autor del Post")
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=250, verbose_name='Título', help_text="Título del Post, max. 250 caracteres")
    enable_comments = models.BooleanField(default=True, verbose_name='Comentarios', help_text="Permitir comentarios")
    excerpt = models.TextField(blank=True, verbose_name='Resumen', help_text="Resumen del Post")
    body = models.TextField(verbose_name='Body', help_text="Cuerpo del Post")
    pub_date = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Publicación', help_text="Fecha de Publicación del Post")
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique_for_date = 'pub_date', verbose_name='Slug', help_text="Direcciónes para el trabajo SEO")
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    tags = TaggableManager()
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)
    
    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, force_update)
    
    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-pub_date']
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/%s/' %(self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
    