from django.shortcuts import get_object_or_404, render_to_response
from blogman.models import Entry

def entries_index(request):
    return render_to_response('blogman/entryndex.html',
                              {'entry_list': Entry.objects.filter(status=Entry.LIVE_STATUS)})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blogman/category_detail.html',
                              {'object_list':category.live_entry_set.all(),
                               'category': category })
    """
        other option with object_list object
        return object_list(request, queryset=category.entry_set.all(),
                       extra_context = {'category':category})
    """