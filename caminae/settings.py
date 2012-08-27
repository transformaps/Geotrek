import os

from django.contrib.messages import constants as messages


gettext_noop = lambda s: s

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

LANGUAGES = (
    ('en', gettext_noop('English')),
    ('fr', gettext_noop('French')),
    ('it', gettext_noop('Italian')),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT_PATH, 'locale'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

AUTH_PROFILE_MODULE = 'authent.UserProfile'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.yui.YUICSSFilter'
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.yui.YUIJSFilter'
]
COMPRESS_YUI_BINARY = '/usr/bin/yui-compressor'


# Make this unique, and don't share it with anybody.
SECRET_KEY = '4b1f@)*y$hobaevq9j&amp;hdph%&amp;!go0ud1qn0a)2&amp;l$np*el3uj&amp;'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'caminae.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'caminae.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

    'caminae.core.context_processors.settings',
)

#
# /!\ Application names (last levels) must be unique
# (c.f. auth/authent)
# https://code.djangoproject.com/ticket/12288
#
PROJECT_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
#    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.gis',

    'south',
    'modeltranslation',
    'leaflet',
    'floppyforms',
    'crispy_forms',
    'compressor',
    'djgeojson',
)

INSTALLED_APPS = PROJECT_APPS + (
    'caminae.authent',
    'caminae.common',
    'caminae.core',
    'caminae.maintenance',
    'caminae.land',
    'caminae.trekking',
    'caminae.infrastructure',
    'caminae.mapentity',
)

SERIALIZATION_MODULES = {
    'geojson' : 'djgeojson.serializers'
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    # The fat backend is used to store big chunk of data (>1 Mo)
    'fat': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'caminae': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

TITLE = gettext_noop("Caminae")
DEFAULT_STRUCTURE_NAME = None
SRID = None
SPATIAL_EXTENT = None

# API projection (client-side), can differ from SRID (database)
API_SRID = 4326

SNAP_DISTANCE = 30  # Distance of snapping in pixels

LEAFLET_CONFIG = {
    "TILES_URL" : [
        ("IGN", 'http://geobi.makina-corpus.net/ecrins-sentiers-tiles/ign/{z}/{x}/{y}.png',),
        ("Ortho", 'http://geobi.makina-corpus.net/ecrins-sentiers-tiles/ortho/{z}/{x}/{y}.png'),
    ],
    "MAX_RESOLUTION" : 1142.7383,
    "TILES_EXTENT" : [700000,6325197,1060000,6617738],
    "SPATIAL_EXTENT" : [5.0, 43.8, 7.5, 45.8],
}

MODELTRANSLATION_TRANSLATION_REGISTRY = 'caminae.translation'

UPLOAD_DIR = 'upload'

# Navigation history tabs
HISTORY_ITEMS_MAX = 7

MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success',
    messages.INFO: 'alert-info',
    messages.DEBUG: 'alert-info',
    messages.WARNING: 'alert-error',
    messages.ERROR: 'alert-error',
}