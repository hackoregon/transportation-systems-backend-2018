
from django.conf.urls import url, include
from django.urls import path

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Hack Oregon 2018 Transportation Systems APIs')

urlpatterns = [
    url(r'^transportation-systems', schema_view),
    url(r'^transportation-systems/passenger_census/', include('passenger_census_api.urls')),
    url(r'^transportation-systems/safety_hotline/', include('safety_hotline_api.urls')),
    url(r'^transportation-systems/biketown/', include('biketown_api.urls')),
    url(r'^transportation-systems/trimet_stop_events/', include('trimet_stop_event_api.urls')),
    url(r'^transportation-systems/trimet_gis/', include('trimet_gis_api.urls')),
]
