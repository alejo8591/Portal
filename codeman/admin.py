from django.contrib import admin
from django.conf import settings
from codeman.models import Language, Snippet

class LanguageAdmin(admin.ModelAdmin):
          class Media:
            js = [
                 settings.STATIC_URL +'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                 settings.STATIC_URL+ 'grappelli/tinymce_setup/tinymce_setup.js'
            ]

class SnippetAdmin(admin.ModelAdmin):
          class Media:
            js = [
                 settings.STATIC_URL +'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                 settings.STATIC_URL+ 'grappelli/tinymce_setup/tinymce_setup.js'
            ]

admin.site.register(Language, LanguageAdmin)
admin.site.register(Snippet, SnippetAdmin)