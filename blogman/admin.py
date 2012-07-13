from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from blogman.models import Category, Entry

class FlatPageAdmin(FlatPageAdminOld):
    class Media:
        js = ('/Users/alejo8591/Documents/portal/Portal/portal/static/tiny_mce/tiny_mce.js',
              '/Users/alejo8591/Documents/portal/Portal/portal/static/tiny_mce/textareas.js',)
        
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['slug']}
    
class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['slug'] }
        
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)