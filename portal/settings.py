# Django settings for portal project.
#parameter config
import dj_database_url
import os
ROOT_CONF = os.path.dirname(os.path.realpath(__file__))
__version__ = "0.0.9"
__status__ = "alpha"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('Alejandro Romero', 'alejo8591@gmail.com'),
)
# for spam email
MANAGERS = (
    ('Alejandro Romero', 'alejo8591@gmail.com'),
)

MANAGERS = ADMINS
#DB system
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'portal',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': '3193115',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

# system time zone.
TIME_ZONE = 'America/Bogota'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es_es'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
#statics files
MEDIA_ROOT = ROOT_CONF + '/uploads/'
MEDIA_URL = '/uploads/'
STATIC_ROOT = ROOT_CONF + '/static/'
STATIC_URL = '/static'
ADMIN_MEDIA_PREFIX = STATIC_URL + '/grappelli/'
# Additional locations of static files
STATICFILES_DIRS = (
    (ROOT_CONF + '/static_files/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '130#m21d6%89d$r4v@p$bppm2u7imnpn%0v4$&amp;jrz=#+3=0tl3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'portal.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'portal.wsgi.application'

TEMPLATE_DIRS = (
     (ROOT_CONF + '/templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.comments',
    'django.contrib.markup',
    'grappelli',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'south',
    # ------ in test -------
    #'tagging',
    'taggit',
    # 'django.contrib.admindocs',
    'blogman',
    'codeman',
)

GRAPPELLI_ADMIN_TITLE = "<li class='user-options-container collapse closed'> \
<a href='javascript://' class='user-options-handler collapse-handler'> \
Portal %s</a><ul class='user-options'><li><a href='/' \
style='padding:10px;'>Back to site</a></li></ul></li>" % (__version__)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
#Akismet api key
AKISMET_API_KEY = '6683e7b5e67b'
# TinyMCE
TINYMCE_JS_URL = os.path.join(STATIC_ROOT, "tiny_mce/tiny_mce.js")
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True