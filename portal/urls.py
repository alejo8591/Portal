from django.conf.urls import patterns, include, url
from blogman.views import entries_index
from django.conf import settings
from blogman.feeds import LatestEntriesFeed
from codeman.views import languages

feeds = { 'entries': LatestEntriesFeed }

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.views.generic.date_based import object_detail

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^blogman/', include('blogman.urls.entries')),
    (r'^blogman/categories/', include('blogman.urls.categories')),
    (r'^blogman/links/', include('blogman.urls.links')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^blogman/feeds/$', LatestEntriesFeed()),
    (r'^languages/', include('codeman.urls.languages')),
    (r'^snippets/', include('codeman.urls.snippets')),
    (r'^', include('django.contrib.flatpages.urls')),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    )