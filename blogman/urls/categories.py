from django.conf.urls import patterns, url, include
#from django.conf.urls.defaults import *
from blogman.models import Category

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list',
     {'queryset': Category.objects.all()}),
    (r'^(?P<slug>[-\w]+)/$', 'blogman.views.category_detail'),
)