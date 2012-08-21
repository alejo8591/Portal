# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
#from django.conf.urls import patterns, url, include
from django.views.generic.list_detail import object_detail, object_list
from codeman.models import Snippet

snippet_query = {'queryset':Snippet.objects.all()}
urlpatterns = patterns('',
    url(r'^$', object_list, dict(snippet_query, paginate_by=10), name='codeman_snippet_list'),
    url(r'^(P<object_id>\d+)/$', object_detail, snippet_query, 'codeman_snippet_detail'),
)