# -*- coding: utf-8 -*-
'''
Settings file for uds server (Django)
'''
from __future__ import unicode_literals

import os
import sys
import django
import django.conf.global_settings as DEFAULT_SETTINGS

# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
BASE_DIR = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1])  # If used 'relpath' instead of abspath, returns path of "enterprise" instead of "openuds"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # For testing begind a reverse proxy

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB; SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;',
            # 'init_command': 'SET storage_engine=INNODB, SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED',
            # 'init_command': 'SET storage_engine=MYISAM, SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED',
        },
        'NAME': 'uds',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
	    # 'CONN_MAX_AGE': 600,		     # Enable DB Pooling, 10 minutes max connection duration
    }
}
ALLOWED_HOSTS = '*'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.

# TIME_SECTION_START
TIME_ZONE = 'Europe/Madrid'
# TIME_SECTION_END

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

ugettext = lambda s: s

LANGUAGES = (
  ('es', ugettext('Spanish')),
  ('en', ugettext('English')),
  ('fr', ugettext('French')),
  ('de', ugettext('German')),
  ('pt', ugettext('Portuguese')),
  ('it', ugettext('Italian')),
  ('eu', ugettext('Basque')),
  ('ca', ugettext('Catalan')),
)

LANGUAGE_COOKIE_NAME = 'uds_lang'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

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
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
# ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'uds_response_cache',
        'OPTIONS': {
            'MAX_ENTRIES': 5000,
            'CULL_FREQUENCY': 3,  #  0 = Entire cache will be erased once MAX_ENTRIES is reached, this is faster on DB. if other value, will remove 1/this number items fromm cache
        }
    },
#    'memory': {
#        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#    }
    'memory': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Related to file uploading
FILE_UPLOAD_PERMISSIONS = 0o640
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o750
FILE_UPLOAD_MAX_MEMORY_SIZE = 512 * 1024  # 512 Kb

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's5ky!7b5f#s35!e38xv%e-+iey6yi-#630x)kk3kk5_j8rie2*'
# This is a very long string, an RSA KEY (this can be changed, but if u loose it, all encription will be lost)
RSA_KEY = '-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQC0qe1GlriQbHFYdKYRPBFDSS8Ne/TEKI2mtPKJf36XZTy6rIyH\nvUpT1gMScVjHjOISLNJQqktyv0G+ZGzLDmfkCUBev6JBlFwNeX3Dv/97Q0BsEzJX\noYHiDANUkuB30ukmGvG0sg1v4ccl+xs2Su6pFSc5bGINBcQ5tO0ZI6Q1nQIDAQAB\nAoGBAKA7Octqb+T/mQOX6ZXNjY38wXOXJb44LXHWeGnEnvUNf/Aci0L0epCidfUM\nfG33oKX4BMwwTVxHDrsa/HaXn0FZtbQeBVywZqMqWpkfL/Ho8XJ8Rsq8OfElrwek\nOCPXgxMzQYxoNHw8V97k5qhfupQ+h878BseN367xSyQ8plahAkEAuPgAi6aobwZ5\nFZhx/+6rmQ8sM8FOuzzm6bclrvfuRAUFa9+kMM2K48NAneAtLPphofqI8wDPCYgQ\nTl7O96GXVQJBAPoKtWIMuBHJXKCdUNOISmeEvEzJMPKduvyqnUYv17tM0JTV0uzO\nuDpJoNIwVPq5c3LJaORKeCZnt3dBrdH1FSkCQQC3DK+1hIvhvB0uUvxWlIL7aTmM\nSny47Y9zsc04N6JzbCiuVdeueGs/9eXHl6f9gBgI7eCD48QAocfJVygphqA1AkEA\nrvzZjcIK+9+pJHqUO0XxlFrPkQloaRK77uHUaW9IEjui6dZu4+2T/q7SjubmQgWR\nZy7Pap03UuFZA2wCoqJbaQJAUG0FVrnyUORUnMQvdDjAWps2sXoPvA8sbQY1W8dh\nR2k4TCFl2wD7LutvsdgdkiH0gWdh5tc1c4dRmSX1eQ27nA==\n-----END RSA PRIVATE KEY-----'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'uds.core.util.Config.context_processor',
                'uds.core.util.html.context',
                'django.template.context_processors.request',
            ],
            'debug': DEBUG,
        },
    },
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'uds.core.util.request.GlobalRequestMiddleware',
    'uds.core.util.middleware.XUACompatibleMiddleware',
]

"""MIDDLEWARE= [
     'django.middleware.security.SecurityMiddleware',
     'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'uds.core.util.request.GlobalRequestMiddleware',
    'uds.core.util.middleware.XUACompatibleMiddleware',
    #'uds.plugins.enterprise.middleware.Middleware',
]"""



SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_COOKIE_HTTPONLY = False
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


ROOT_URLCONF = 'server.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'server.wsgi.application'

INSTALLED_APPS = (
     'django.contrib.contenttypes', # Not used
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'uds',
)

# Compressor settings (for css/js)
COMPRESS_ENABLED = not DEBUG
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
    # ('text/stylus', 'stylus < {infile} > {outfile}'),
    # ('text/foobar', 'path.to.MyPrecompilerFilter'),
)
if DEBUG:
    COMPRESS_DEBUG_TOGGLE = 'debug'
#   
# Enable this if you need to allow round robin load balancing of web server
# This is so because we need to share the files between servers
# Another options is put /var/server/static on a shared nfs forder for all servers
#   
# COMPRESS_STORAGE = 'uds.core.util.FileStorage.CompressorFileStorage'

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGDIR = BASE_DIR + '/' + 'log'
LOGFILE = 'uds.log'
SERVICESFILE = 'services.log'
WORKERSFILE = 'workers.log'
AUTHFILE = 'auth.log'
USEFILE = 'use.log'
TRACEFILE = 'trace.log'
LOGLEVEL = DEBUG and 'DEBUG' or 'INFO'
ROTATINGSIZE = 32 * 1024 * 1024  # 32 Megabytes before rotating files

# Tests runner is default tests runner
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(lineno)d %(message)s'
        },
        'database': {
            'format': '%(levelname)s %(asctime)s Database %(message)s'
        },
        'auth': {
            'format': '%(asctime)s %(message)s'
        },
        'use': {
            'format': '%(asctime)s %(message)s'
        },
        'trace': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },

        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': LOGDIR + '/' + LOGFILE,
            'mode': 'a',
            'maxBytes': ROTATINGSIZE,
            'backupCount': 3,
            'encoding': 'utf-8'
        },

        'database': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': LOGDIR + '/' + 'sql.log',
            'mode': 'a',
            'maxBytes': ROTATINGSIZE,
            'backupCount': 3,
            'encoding': 'utf-8'
        },

        'servicesFile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': LOGDIR + '/' + SERVICESFILE,
            'mode': 'a',
            'maxBytes': ROTATINGSIZE,
            'backupCount': 3,
            'encoding': 'utf-8'
        },

        'workersFile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': LOGDIR + '/' + WORKERSFILE,
            'mode': 'a',
            'maxBytes': ROTATINGSIZE,
            'backupCount': 3,
            'encoding': 'utf-8'
        },

        'authFile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'auth',
            'filename': LOGDIR + '/' + AUTHFILE,
            'mode': 'a',
            'maxBytes': ROTATINGSIZE,
            'backupCount': 3,
            'encoding': 'utf-8'
        },

        'useFile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'use',
            'filename': LOGDIR + '/' + USEFILE,
            'mode': 'a',
            'maxBytes': ROTATINGSIZE,
            'backupCount': 3,
            'encoding': 'utf-8'
        },

        'traceFile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'trace',
            'filename': LOGDIR + '/' + TRACEFILE,
            'mode': 'a',
            'maxBytes': ROTATINGSIZE,
            'backupCount': 3,
            'encoding': 'utf-8'
        },

        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['database'],
            'level': 'DEBUG',
            'propagate': False,
        },

        'uds': {
            'handlers': ['file'],
            'level': LOGLEVEL,
        },

        'uds.core.workers': {
            'handlers': ['workersFile'],
            'level': LOGLEVEL,
            'propagate': False,
        },
        'uds.core.jobs': {
            'handlers': ['workersFile'],
            'level': LOGLEVEL,
            'propagate': False,
        },

        'uds.services': {
            'handlers': ['servicesFile'],
            'level': LOGLEVEL,
            'propagate': False,
        },
        # Custom Auth log
        'authLog': {
            'handlers': ['authFile'],
            'level': 'INFO',
            'propagate': False,
        },
        # Custom Services use log
        'useLog': {
            'handlers': ['useFile'],
            'level': 'INFO',
            'propagate': False,
        },
        # Custom tracing
        'traceLog': {
            'handlers': ['traceFile'],
            'level': 'INFO',
            'propagate': False,
        }

    }
}