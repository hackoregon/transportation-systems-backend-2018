from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from odot_crash_api import views

# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'crashes', views.CrashViewSet)
router.register(r'participants', views.ParticipantViewSet)
router.register(r'vehicles', views.VehicleViewSet)

# schema_view = get_swagger_view(title='Hack Oregon 2018 Transportation Systems APIs')

urlpatterns = [
    # url(r'^schema/', schema_view),
    url(r'^', include(router.urls)),
    # url(r'^api/', include(router.urls)),
]
