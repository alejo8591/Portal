from django.conf.urls import patterns, include, url
from blogman.views import entries_index 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^portal/', include('portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^blogman/', 'blogman.views.entries_index'),
    url(r'^blogman/(?P<year>\d{4})/(?P<month>\w{4})/(?P<day>\d{2})/(?P<e_slug>[-\w]+)/$',
        'blogman.views.entry_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.flatpages.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
        )