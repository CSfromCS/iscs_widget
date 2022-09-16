"""widget_father_when_can_i_be_on_my_own_i_have_the_hello_world_to_see URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from homepage.views import WidgetUserCreateView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='homepage/')),
    path('homepage/', include("homepage.urls", namespace='homepage')),
    path('users/add', WidgetUserCreateView.as_view(), name='widgetuser_form'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
