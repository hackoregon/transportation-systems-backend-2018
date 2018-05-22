
from django.conf.urls import url, include
from django.urls import path

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Hack Oregon 2018 Transportation Systems APIs')

urlpatterns = [
    url(r'^swagger/', schema_view),
    url(r'^transportation_systems_2018/passenger_census/', include('passenger_census_api.urls')),
    url(r'^transportation_systems_2018/safety_hotline/', include('safety_hotline_api.urls')),
    url(r'^transportation_systems_2018/biketown/', include('biketown_api.urls')),
    url(r'^transportation_systems_2018/trimet_stop_events/', include('trimet_stop_event_api.urls')),
    url(r'^transportation_systems_2018/trimet_gis/', include('trimet_gis_api.urls')),
]
