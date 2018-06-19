from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from pudl_sensors_api import views


router = DefaultRouter()
router.register(r'sensor/locations', views.SensorLocationsViewSet)




urlpatterns = [
    url(r'^', include(router.urls)),
]
