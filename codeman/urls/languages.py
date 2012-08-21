from django.conf.urls import patterns, url, include
from django.views.generic.list_detail import object_list
from codeman.models import Language
from codeman.views.languages import language_detail

language_info = {
    'queryset': Language.objects.all(),
    'paginate_by': 10
}
urlpatterns = patterns('',
                       url(r'^', object_list, language_info, name='codeman_language_list'),
                       url(r'^(?P<slug>[-\w]+)/$', language_detail, name='codeman_language_detail'),
)