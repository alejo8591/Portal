from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from blogman.models import Category, Entry
from django.conf import settings

class FlatPageAdmin(FlatPageAdminOld):
    class Media:
        pass
        #js = ('%tiny_mce/tiny_mce.js' % settings.STATIC_URL,)
        
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['slug']}
    
class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['slug'] }
    Entry.objects.all()
        
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)