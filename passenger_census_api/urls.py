from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from passenger_census_api import views
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'', views.PassengerCensusViewSet)
router.register(r'routes', views.PassengerCensusRoutesViewSet, base_name='passenger-census')
router.register(r'national/ridership', views.NationalTotalsViewSet, base_name='passenger-census')
router.register(r'service-availability', views.ServiceAvailabilityViewSet, base_name='passenger-census')
router.register(r'', views.PassengerCensusRetrieveViewSet)

router.register(r'routes/busses/averages', views.PassengerCensusAnnualBussesAvgViewSet, base_name='passenger-census')

router.register(r'routes/trains/averages', views.PassengerCensusAnnualTrainsAvgViewSet, base_name='passenger-census')

router.register(r'routes/street-car/averages', views.PassengerCensusAnnualStreetCarAvgViewSet, base_name='passenger-census')
# No tram census in database
# router.register(r'routes/tram/averages', views.PassengerCensusAnnualTramAvgViewSet, base_name='passenger-census')

router.register(r'routes/annual/total', views.PassengerCensusRoutesAnnualTotalViewSet, base_name='passenger-census')
router.register(r'routes/annual/averages', views.PassengerCensusRoutesAnnualAvgViewSet, base_name='passenger-census')
router.register(r'routes/annual/differences', views.AnnualRouteDifferencesViewSet, base_name='passenger-census')
router.register(r'census-block/oregon/polygons', views.OrCensusBlockPolygonsViewSet, base_name='passenger-census')
router.register(r'census-block/washington/polygons', views.WaCensusBlockPolygonsViewSet, base_name='passenger-census')
router.register(r'census-block/totals', views.AnnualCensusBlockRidershipViewSet, base_name='passenger-census')
router.register(r'census-block/change', views.CensusBlockChangeViewSet, base_name='passenger-census')
router.register(r'routes/change', views.RouteChangeViewSet, base_name='passenger-census')
router.register(r'census/info', views.PassengerCensusInfoViewSet, base_name='passenger-census')

router.register(r'system/annual/total', views.PassengerCensusAnnualSystemTotalViewSet, base_name='passenger-census')
router.register(r'system/annual/averages', views.PassengerCensusAnnualSystemAvgViewSet, base_name='passenger-census')
# schema_view = get_swagger_view(title='Hack Oregon 2018 Transportation Systems APIs')

urlpatterns = [
    # url(r'^schema/', schema_view),
    url(r'^', include(router.urls)),
    url(r'^routes/(?P<pk>[0-9]+)/$', views.RouteDetail.as_view()),
    url(r'^national/(?P<pk>[0-9]+)/$', views.NationalDetail.as_view())

]
