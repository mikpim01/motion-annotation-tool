"""
Django settings for proj project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import os
import platform

ADMINS = [
    ('Your Name', 'you@server.com'),
]

DEFAULT_FROM_EMAIL = 'you@server.com'
SERVER_EMAIL = 'you@server.com'

INSTALLED_APPS = [
    'dataset.apps.DatasetConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_archive',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'proj.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_THOUSAND_SEPARATOR = False

USE_TZ = True

ARCHIVE_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'backups'))

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'dataset.auth.EmailBackend',
    'dataset.auth.RedmineBackend',
)

# If you don't want to use Redmine for authentication, simply remove `dataset.auth.RedmineBackend`
# from above.
REDMINE_AUTH_REST_URL = 'https://yourdomain.com/redmine/users/current.json?include=memberships'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
        'ATOMIC_REQUESTS': False,
        'OPTIONS': {
            'timeout': 20,  # in seconds
        },
    }
}

DEBUG = True
ALLOWED_HOSTS = []

# Security
SECRET_KEY = '=cer0o*_u!#luitbd6tnx^drp_jnd2@#7ps9un7_o7lr$qa#%e'

# Static
STATIC_URL = '/static/'

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'handlers': {
        'console': {
            # logging handler that outputs log messages to terminal
            'class': 'logging.StreamHandler',
            'level': 'DEBUG', # message level to be written to console
        },
    },
    'loggers': {
        '': {
            # this sets root level logger to log debug and higher level
            # logs to console. All other loggers inherit settings from
            # root level logger.
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False, # this tells logger to send logging message
                                # to its parent (will send if set to True)
        },
        # 'django.db': {
        #     # django also has database level logging
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': False, # this tells logger to send logging message
        #                         # to its parent (will send if set to True)
        # },
    },
}

# SRILM
if platform.platform().startswith('Darwin'):
    SRILM_ROOT_PATH = '/Users/matze/Studium/Faecher/PdF/srilm'
    SRILM_BIN_PATH = os.path.join(SRILM_ROOT_PATH, 'bin', 'macosx')
else:
    SRILM_ROOT_PATH = '/home/SMBAD/plappert/srilm'
    SRILM_BIN_PATH = os.path.join(SRILM_ROOT_PATH, 'bin', 'i686-m64')
assert os.path.isdir(SRILM_BIN_PATH)
