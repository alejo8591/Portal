# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Título', help_text="Título del Post, max. 250 caracteres")
    
