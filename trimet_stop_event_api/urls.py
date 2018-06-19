from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from trimet_stop_event_api import views

# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'trimet-stop-events', views.TrimetStopEventsViewSet)
router.register(r'totals', views.TotalOnsByHourViewSet)
router.register(r'disturbance-stops', views.DisturbanceStopsViewSet)


# schema_view = get_swagger_view(title='Hack Oregon 2018 Transportation Systems APIs')

urlpatterns = [
    # url(r'^schema/', schema_view),
    url(r'^', include(router.urls)),
    # url(r'^api/', include(router.urls)),
]
