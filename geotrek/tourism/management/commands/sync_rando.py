# -*- encoding: UTF-8

from django.conf import settings
from django.utils import translation
from optparse import make_option
import os
from zipfile import ZipFile

from geotrek.tourism import (models as tourism_models,
                             views as tourism_views)
from geotrek.tourism.views import TrekTouristicContentViewSet,\
    TrekTouristicEventViewSet
from geotrek.trekking.management.commands.sync_rando import Command as BaseCommand


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--with-touristicevents',
                    '-w',
                    action='store_true',
                    dest='with-events',
                    default=False,
                    help='include touristic events'),
        make_option('--with-touristiccontent-categories',
                    '-c',
                    action='store',
                    dest='content-categories',
                    default=None,
                    help='include touristic categories separated by commas'),
    )

    def handle(self, *args, **options):
        self.with_events = options.get('with-events', False)
        self.categories = None

        if options.get('content-categories', u""):
            self.categories = options.get('content-categories', u"").split(',')

        super(Command, self).handle(*args, **options)

    def sync_content(self, lang, content, zipfile=None):
        self.sync_pdf(lang, content)

        for picture, resized in content.resized_pictures:
            self.sync_media_file(lang, resized, zipfile=zipfile)

    def sync_event(self, lang, event, zipfile=None):
        self.sync_pdf(lang, event)

        for picture, resized in event.resized_pictures:
            self.sync_media_file(lang, resized, zipfile=zipfile)

    def sync_tourism(self, lang):
        self.sync_geojson(lang, tourism_views.TouristicContentViewSet, 'touristiccontents',)
        self.sync_geojson(lang, tourism_views.TouristicEventViewSet, 'touristicevents',)

        contents = tourism_models.TouristicContent.objects.existing().order_by('pk')
        contents = contents.filter(**{'published_{lang}'.format(lang=lang): True})
        if self.source:
            contents = contents.filter(source__name__in=self.source)
        for content in contents:
            self.sync_content(lang, content)

        events = tourism_models.TouristicEvent.objects.existing().order_by('pk')
        events = events.filter(**{'published_{lang}'.format(lang=lang): True})
        if self.source:
            events = events.filter(source__name__in=self.source)
        for event in events:
            self.sync_event(lang, event)

    def sync_trek_touristiccontents(self, lang, trek, zipfile=None):
        params = {'format': 'geojson',
                  'categories': ','.join(category for category in self.categories), }

        view = TrekTouristicContentViewSet.as_view({'get': 'list'})
        name = os.path.join('api', lang, 'treks', str(trek.pk), 'touristiccontents.geojson')
        self.sync_view(lang, view, name, params=params, zipfile=zipfile, pk=trek.pk)

    def sync_trek_touristicevents(self, lang, trek, zipfile=None):
        params = {'format': 'geojson', }
        view = TrekTouristicEventViewSet.as_view({'get': 'list'})
        name = os.path.join('api', lang, 'treks', str(trek.pk), 'touristicevents.geojson')
        self.sync_view(lang, view, name, params=params, zipfile=zipfile, pk=trek.pk)

    def sync(self):
        super(Command, self).sync()

        self.sync_static_file('**', 'tourism/touristicevent.svg')
        self.sync_pictograms('**', tourism_models.InformationDeskType)
        self.sync_pictograms('**', tourism_models.TouristicContentCategory)
        self.sync_pictograms('**', tourism_models.TouristicContentType)
        self.sync_pictograms('**', tourism_models.TouristicEventType)

        for lang in settings.MODELTRANSLATION_LANGUAGES:
            translation.activate(lang)
            self.sync_tourism(lang)

    def sync_trek(self, lang, trek):
        super(Command, self).sync_trek(lang, trek)
        # reopen trek zip and add custom info if needed
        zipname = os.path.join('zip', 'treks', lang, '{pk}.zip'.format(pk=trek.pk))
        zipfullname = os.path.join(self.tmp_root, zipname)
        self.trek_zipfile = ZipFile(zipfullname, 'a')

        if self.with_events:
            self.sync_trek_touristicevents(lang, trek, zipfile=self.trek_zipfile)

        if self.categories:
            self.sync_trek_touristiccontents(lang, trek, zipfile=self.trek_zipfile)

        self.close_zip(self.trek_zipfile, zipname)
