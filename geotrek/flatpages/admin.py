from django.contrib import admin
from django.conf import settings

from modeltranslation.admin import TranslationAdmin

from geotrek.flatpages import models as flatpages_models


class FlatPagesAdmin(TranslationAdmin):
    list_display = ('title', 'published', 'publication_date', 'target')
    search_fields = ('title', 'content')


if settings.FLATPAGES_ENABLED:
    admin.site.register(flatpages_models.FlatPage, FlatPagesAdmin)