# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from markdown import markdown
from django.contrib.comments.models import Comment
from akismet import Akismet
from django.contrib.sites.models import Site
from django.utils.encoding import smart_str
from django.contrib.comments.signals import comment_will_be_posted

class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Título', help_text="Título de la Categoria, max. 250 caracteres")
    slug = models.SlugField(unique=True, verbose_name='Slug', help_text="Direcciónes para el trabajo SEO")
    description = models.TextField(verbose_name='Descripción', help_text="Descripción del articulo")
    
    def live_entry_set(self):
        from blogman.models import Entry
        return self.entry_set.filter(status=Entry.LIVE_STATUS)
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"
        
    def get_absolute_url(self):
        return "/categories/%s/" % self.slug
    
    def __unicode__(self):
        return self.title
    
class LiveEntryManager(models.Manager):
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)
        
class Entry(models.Model):
    # Constants for model Entry refer to a Status post
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    # Options of status
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
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
    
    # Use model manager for Live Entry or Post
    objects = models.Manager()
    live = LiveEntryManager()
    
    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-pub_date']
    
    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, force_update)
   
    @models.permalink
    def get_absolute_url(self):
        return ('blogman_entry_detail', (), {
            'year': self.pub_date.strftime('%Y'),
            'month': self.pub_date.strftime('%b').lower(),
            'day': self.pub_date.strftime('%d'),
            'slug': self.slug
        })
    #get_absolute_url = models.permalink(get_absolute_url)
    
    live = LiveEntryManager()
    objects = models.Manager()
    
    
class Link(models.Model):
    title = models.CharField(max_length=250, verbose_name='Título', help_text="Título del Link, max. 250 caracteres")
    description = models.TextField(verbose_name='Descripción', help_text="Descripción del Link")
    description_html = models.TextField(verbose_name='Descripción HTML', help_text="Descripción del Link en HTML")
    url = models.URLField(unique=True)
    posted_by = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')
    tags = TaggableManager()
    enable_comments = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-pub_date']
    

    def __unicode__(self):
        return self.title
        
        
    @models.permalink
    def get_absolute_url(self):
        return ('blogman_entry_detail', (), {
            'year': self.pub_date.strftime('%Y'),
            'month': self.pub_date.strftime('%b').lower(),
            'day': self.pub_date.strftime('%d'),
            'slug': self.slug
        })

def moderate_comment(sender, instance, **kwargs):
    if not instance.id:
        entry = instance.content_object
        delta = datetime.now() - entry.pub_date
        if delta.days > 30:
            instance.is_public = False
        else:
            current_site = Site.objects.get_current()
            akismet_api = Akismet(key=settings.AKISMET_API_KEY, blog_url="http://%s/" %current_site.domain)
            if akismet_api.verify_key():
                akismet_data = {'comment_type':'comment',
                                'referrer':'',
                                'user_ip':instance.ipd_address,
                                'user_agent':''}
                if akismet_api.comment_check(smart_str(instance.comment),
                                             akismet_data,
                                             build_data=True):
                    instance.is_public = False    
        
        
comment_will_be_posted.connect(moderate_comment, sender=Comment)