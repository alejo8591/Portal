from django.contrib import admin
from django.conf import settings
from codeman.models import Language, Snippet

admin.site.register(Language)
admin.site.register(Snippet)