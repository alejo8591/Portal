from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list
from codeman.models import Language

def language_detail(request, slug):
    language = get_object_or_404(Language, slug=slug)
    return object_list(request,
                       queryset=language.snippet_set.all(),
                       paginate_by =10,
                       template_name='codeman/language_detail.html',
                       extra_context={'language': language})