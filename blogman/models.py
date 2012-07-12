# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# ----- tagging in test
#from tagging.fields import TagField
from taggit.managers import TaggableManager
from markdown import markdown

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
        return self.b_title
    
class Entry(models.Model):
    STATUS_CHOICES = (
        (1, 'Live'),
        (2, 'Draft'),
        (3, 'Hidden'),
    )
    e_author = models.ForeignKey(User, verbose_name='Autor', help_text="Nombre del Autor del Post")
    e_category = models.ManyToManyField(Category)
    e_title = models.CharField(max_length=250, verbose_name='Título', help_text="Título del Post, max. 250 caracteres")
    e_enable_comments = models.BooleanField(default=True, verbose_name='Comentarios', help_text="Permitir comentarios")
    e_excerpt = models.TextField(blank=True, verbose_name='Resumen', help_text="Resumen del Post")
    e_body = models.TextField(verbose_name='Body', help_text="Cuerpo del Post")
    e_pub_date = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Publicación', help_text="Fecha de Publicación del Post")
    e_featured = models.BooleanField(default=False)
    e_slug = models.SlugField(unique_for_date = 'e_pub_date', verbose_name='Slug', help_text="Direcciónes para el trabajo SEO")
    e_status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    e_tags = TaggableManager()
    e_excerpt_html = models.TextField(editable=False, blank=True)
    e_body_html = models.TextField(editable=False, blank=True)
    
    def save(self, force_insert=False, force_update=False):
        self.e_body_html = markdown(self.e_body)
        if self.e_excerpt:
            self.e_excerpt_html = markdown(self.e_excerpt)
        super(Entry, self).save(force_insert, force_update)
    
    def get_absolute_url(self):
        return "/%s/%s/" % (self.e_pub_date.strftime("%Y/%b/%d").lower(), self.e_slug)
    
    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-e_pub_date']
    
    def __unicode__(self):
        return self.e_title