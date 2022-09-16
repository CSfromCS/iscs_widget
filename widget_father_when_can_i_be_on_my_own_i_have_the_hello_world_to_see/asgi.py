"""
ASGI config for widget_father_when_can_i_be_on_my_own_i_have_the_hello_world_to_see project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'widget_father_when_can_i_be_on_my_own_i_have_the_hello_world_to_see.settings')

application = get_asgi_application()
