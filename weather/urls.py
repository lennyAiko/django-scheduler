from django.urls import re_path, include
from .views import WeatherViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data', WeatherViewset, basename='weather-data')

urlpatterns = [
    re_path('', include(router.urls)),
]