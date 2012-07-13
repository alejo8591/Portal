from django.conf.urls import patterns, include, url
from blogman.views import entries_index
from blogman.models import Entry

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.date_based import object_detail
entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field' : 'pub_date',
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^portal/', include('portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^blogman/$', 'django.views.generic.date_based.archive_index', entry_info_dict),
    url(r'^blogman/(?P<year>\d{4})/$','django.views.generic.date_based.archive_year', entry_info_dict),
    url(r'^blogman/(?P<year>\d{4})/(?P<month>\w{3})/$', 'django.views.generic.date_based.archive_month', entry_info_dict),
    url(r'^blogman/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', entry_info_dict),
    url(r'^blogman/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        'object_detail', entry_info_dict),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    #url(r'^', include('django.contrib.flatpages.urls')),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
        )