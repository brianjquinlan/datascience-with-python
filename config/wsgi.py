"""
WSGI config for datascience-with-python project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.production':
    from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datascience-with-python.settings")

application = get_wsgi_application()
if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.setings.production':
    application = DjangoWhiteNoise(application)
