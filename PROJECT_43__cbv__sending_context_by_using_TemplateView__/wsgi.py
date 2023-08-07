"""
WSGI config for PROJECT_43__cbv__sending_context_by_using_TemplateView__ project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT_43__cbv__sending_context_by_using_TemplateView__.settings')

application = get_wsgi_application()
