
from django.conf.urls import url, include
from django.urls import path

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Hack Oregon 2018 Transportation Systems APIs')

urlpatterns = [
    url(r'^schema/', schema_view),
    url(r'^api/passenger_census/', include('passenger_census_api.urls')),
    url(r'^api/safety_hotline_api/', include('safety_hotline_api.urls')),
]
