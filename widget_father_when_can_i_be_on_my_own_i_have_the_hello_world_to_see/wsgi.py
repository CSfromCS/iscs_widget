"""
WSGI config for widget_father_when_can_i_be_on_my_own_i_have_the_hello_world_to_see project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'widget_father_when_can_i_be_on_my_own_i_have_the_hello_world_to_see.settings')

application = get_wsgi_application()
