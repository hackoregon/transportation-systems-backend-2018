from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from multco_permits_api import views


router = DefaultRouter()
router.register(r'current', views.CurrentPermitsViewSet)
router.register(r'archived', views.ArchivedPermitsViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
]
