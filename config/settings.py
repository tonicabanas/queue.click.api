import os
import sys

import environ

env = environ.Env()

ROOT_DIR = environ.Path(__file__) - 2  # (/a/b/myfile.py - 2 = /)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Admins: Will receive emails when something breaks: django.request, raven, sentry.errors...

ADMINS = ['tonicabanas@queue.click']

# Django conf
SECRET_KEY = env('DJANGO_SECRET_KEY', default='CHANGE ME!!!')

DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS', default='').replace(' ', ',').split(',')

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    # FOR EXAMPLE THIS ONES
    # 'rest_framework',
    # 'django_extensions',
]

LOCAL_APPS = [
    # YOUR APPS
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            ROOT_DIR('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if 'test' not in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'database-develop',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'database-develop',
        }
    }

DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = 500

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = False

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = env('DJANGO_STATIC_ROOT', default=str(ROOT_DIR('staticfiles')))
STATIC_URL = env('DJANGO_STATIC_URL', default='/static/')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Media configuration

MEDIA_ROOT = env('DJANGO_MEDIA_ROOT', default=str(ROOT_DIR('media')))
MEDIA_URL = env('DJANGO_MEDIA_URL', default='/media/')

FILE_UPLOAD_PERMISSIONS = 0o664

# Logging configuration

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s',
        },
        'verbose': {
            '()': 'utils.log.DjangoColorsFormatter',
            'format': "[%(asctime)s] %(levelname)s [%(name)s] [%(pathname)s:%(lineno)s] %(message)s",
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {
            'format': '[%(asctime)s] %(name)s %(levelname)s %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# Fixture configuration

FIXTURE_DIRS = (
    ROOT_DIR('fixtures'),
)

# Email configuration

SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default='root@localhost')

# Debug configuration

if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']

    INTERNAL_IPS = ['127.0.0.1']

    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

# Raven configuration

RAVEN_ENABLED = env.bool('DJANGO_RAVEN_ENABLED', default=False)

if RAVEN_ENABLED:
    import raven as raven

    INSTALLED_APPS += (
        'raven.contrib.django.raven_compat',
    )

    RAVEN_CONFIG = {
        'dsn': env("DJANGO_RAVEN_DSN"),
        'release': raven.fetch_git_sha(ROOT_DIR()),
        'environment': 'production',
    }

    LOGGING['handlers']['sentry'] = {
        'level': 'INFO',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
    }

    LOGGING['root']['handlers'] = ['console', 'sentry']

    LOGGING['loggers']['raven'] = {
        'level': 'DEBUG',
        'handlers': ['console', 'mail_admins'],
        'propagate': False,
    }

    LOGGING['loggers']['sentry.errors'] = {
        'level': 'DEBUG',
        'handlers': ['console', 'mail_admins'],
        'propagate': False,
    }

# Test configuration

if 'test' in sys.argv:
    # Put here any configuration that you want to change or set only for testing purposes
    pass
