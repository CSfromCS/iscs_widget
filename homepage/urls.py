from django.urls import path
from .views import HomepageView, WidgetUserDetailView, WidgetUserCreateView

urlpatterns = [
    path('', HomepageView.as_view(), name='index'),
    path('<int:pk>/details', WidgetUserDetailView.as_view(),
         name='widgetuser_detail'),
]
app_name = "homepage"
