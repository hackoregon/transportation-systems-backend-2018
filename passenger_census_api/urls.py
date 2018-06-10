from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from passenger_census_api import views
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'', views.PassengerCensusViewSet)
router.register(r'routes', views.PassengerCensusRoutesViewSet)

router.register(r'', views.PassengerCensusRetrieveViewSet)
router.register(r'routes/annual/average', views.PassengerCensusRoutesAnnualAvgViewSet, base_name='passenger-census')
router.register(r'routes/annual/total', views.PassengerCensusRoutesAnnualTotalViewSet, base_name='passenger-census')

router.register(r'census/info', views.PassengerCensusInfoViewSet, base_name='passenger-census')

# schema_view = get_swagger_view(title='Hack Oregon 2018 Transportation Systems APIs')

urlpatterns = [
    # url(r'^schema/', schema_view),
    url(r'^', include(router.urls)),
    # url(r'^api/', include(router.urls)),
]
