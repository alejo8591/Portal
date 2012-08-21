from django.conf.urls import patterns, include, url
from blogman.views import entries_index
from django.conf import settings
from blogman.feeds import LatestEntriesFeed

feeds = { 'entries': LatestEntriesFeed }

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.views.generic.date_based import object_detail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^portal/', include('portal.foo.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^blogman/', include('blogman.urls.entries')),
    (r'^blogman/categories/', include('blogman.urls.categories')),
    (r'^blogman/links/', include('blogman.urls.links')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^blogman/feeds/$', LatestEntriesFeed()),
    (r'^snippets/', include('codeman.urls.snippets')),
    (r'^languages/', include('codeman.urls.languages')),
    url(r'^', include('django.contrib.flatpages.urls')),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    )