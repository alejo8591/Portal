# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from pygments import formatters, highlight, lexers
from taggit.managers import TaggableManager
from datetime import datetime, date
from markdown import markdown


class Language(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    language_code = models.CharField(max_length=60)
    mime_type = models.CharField(max_length=60)
    
    class Meta:
        ordering = ['-name']
        
    def __unicode__(self):
        return self.name
    
    def get_lexer(self):
        return lexers.get_lexer_by_name(self.language_code)
    
    @models.permalink
    def get_absolute_url(self):
        return ('codeman_language_detail', (), {'slug': self.slug})
    
class Snippet(models.Model):
    title = models.CharField(max_length=256)
    language = models.ForeignKey('Language')
    author = models.ForeignKey(User)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    code = models.TextField()
    highlighted_code = models.TextField(editable=False)
    tags = TaggableManager()
    pub_date = models.DateTimeField(editable=False)
    update_date = models.DateTimeField(editable=False)
    
    class Meta:
        ordering = ['-pub_date']
        
    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False):
        if not self.id: self.pub_date = datetime.now()
        self.update_date = datetime.now()
        self.description_html = markdown(self.description)
        self.highlighted_code = self.highlight()
        super(Snippet, self).save(force_insert, force_update)
        
    def highlight(self):
        """
            linenos=True argument 
            formatter tells pygments to generate the output with line numbers
            so that it’s easier to read the code and identify
            specific lines.
        """
        return highlight(self.code, self.language.get_lexer(),
                         formatters.HtmlFormatter(linenos=True))
    @models.permalink
    def get_absolute_url(self):
        return ('codeman_snippet_detail', (), {'object_id': self.id})
