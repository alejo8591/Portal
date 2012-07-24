from django.conf.urls import patterns, url, include
#from django.conf.urls.defaults import *
from blogman.models import Entry

entry_info_dict = {
    'queryset': Entry.objects.filter(status=Entry.LIVE_STATUS),
    'date_field' : 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    (r'^$','archive_index', entry_info_dict,
     'blogman_entry_archive_index'),
    (r'^(?P<year>\d{4})/$', 'archive_year',  entry_info_dict,
     'blogman_entry_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$','archive_month',  entry_info_dict,
     'blogman_entry_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day',  entry_info_dict,
     'blogman_entry_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', entry_info_dict,
     'blogman_entry_detail'),
)