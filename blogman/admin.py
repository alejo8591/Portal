from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from blogman.models import Category, Entry
from django.conf import settings

class FlatPageAdmin(FlatPageAdminOld):
      # agregar editor de texto
      class Media:
          js = [
                 settings.STATIC_URL +'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                 settings.STATIC_URL+ 'grappelli/tinymce_setup/tinymce_setup.js'
           ]
           
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['slug']}
    class Media:
          js = [
                 settings.STATIC_URL +'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                 settings.STATIC_URL+ 'grappelli/tinymce_setup/tinymce_setup.js'
           ]
    
class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['slug'] }
    class Media:
          js = [
                 settings.STATIC_URL +'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                 settings.STATIC_URL+ 'grappelli/tinymce_setup/tinymce_setup.js'
           ]        
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)