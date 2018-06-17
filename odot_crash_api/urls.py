from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from odot_crash_api import views


router = DefaultRouter()
router.register(r'crashes', views.CrashViewSet)
router.register(r'participants', views.ParticipantViewSet)
router.register(r'vehicles', views.VehicleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
