"""
ASGI config for PROJECT_43__cbv__sending_context_by_using_TemplateView__ project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT_43__cbv__sending_context_by_using_TemplateView__.settings')

application = get_asgi_application()
