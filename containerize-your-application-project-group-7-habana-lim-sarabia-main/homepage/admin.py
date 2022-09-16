from django.contrib import admin

from .models import WidgetUser

# Widget User Model 
class WidgetUserAdmin(admin.ModelAdmin):
    model = WidgetUser

admin.site.register(WidgetUser, WidgetUserAdmin)
