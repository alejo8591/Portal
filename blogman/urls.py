from django.conf.urls import patterns, url, include
from blogman import urls

entry_info_dict = {
    'queryset': Entry.objects.filter(status=Entry.LIVE_STATUS),
    'date_field' : 'pub_date',
}

urlpatterns = patterns('',
    (r'^', include('blogman.urls.entries')),
    (r'^categories/', include('blogman.urls.categories')),
    (r'^links/', include('blogman.urls.links')),
)