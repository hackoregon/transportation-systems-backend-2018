
from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter


from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Hack Oregon 2018 Transportation Systems APIs')

urlpatterns = [
    url(r'^transportation-systems/$', schema_view),
    url(r'^transportation-systems/odot-crash-data/', include('odot_crash_api.urls')),
    url(r'^transportation-systems/passenger-census/', include('passenger_census_api.urls')),
    url(r'^transportation-systems/safety-hotline/', include('safety_hotline_api.urls')),
    url(r'^transportation-systems/biketown/', include('biketown_api.urls')),
    url(r'^transportation-systems/trimet-stop-events/', include('trimet_stop_event_api.urls')),
    url(r'^transportation-systems/multnomah-county-permits/', include('multco_permits_api.urls')),
    url(r'^transportation-systems/origin-destination/', include('origin_destination_api.urls')),
    path('transportation-systems/sandbox/', include('civic_sandbox.urls')),

]
