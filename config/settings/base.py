"""
Django settings for datascience-with-python project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import environ
env = environ.Env()

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('datascience-with-python')

# Debug
DEBUG = env.bool('DJANGO_DEBUG', False)

#ALLOWED_HOSTS = []

# SITEID 
SITE_ID = 1

# Application config
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'taggit',
    'sorl.thumbnail',
    'django_user_agents',
]

LOCAL_APPS = [
    # apps you create go here
    'datascience-with-python.blog',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS 

# middleware config
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

# Database
DATABASES = {
        'default': env.db('DATABASE_URL'), # example 'postgres:///db_name'
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# templates config
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
		    str(APPS_DIR.path('templates'))
		],
        'OPTIONS': {
	    'debug': DEBUG,
	        'loaders' : [
			'django.template.loaders.filesystem.Loader',	
			'django.template.loaders.app_directories.Loader',
	        ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# what's used to send emails
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND')

# admins of site
ADMINS = (
	("""Brian Quinlan""", 'bquinlan8@yahoo.com'),
)

MANAGERS = ADMINS

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    str(APPS_DIR.path('static'))
]

# media
MEDIA_URL = '/media/'
MEDIA_ROOT = str(APPS_DIR('media'))

# url config
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


ADMIN_URL = r'^admin/'

# third party
USER_AGENTS_CACHE = 'default'

# mailchimp keys
MAILCHIMP_API_KEY = env('MAILCHIMP_API_KEY')
MAILCHIMP_SUBSCRIBE_LIST_ID = env('MAILCHIMP_SUBSCRIBE_LIST_ID')
