
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django_filters import filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework_gis.filters import DistanceToPointFilter

from pudl_sensors_api.models import SensorLocations
from pudl_sensors_api.serializers import SensorLocationsSerializer

import coreapi

class SensorLocationsGeoFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into schema.
    """

    class Meta:
        model = SensorLocations
        fields = []

    def get_schema_fields(self, view):
        fields = []
        dist = coreapi.Field(
            name="dist",
            location="query",
            description="Distance in Meters (Use with point)",
            type="number"
            )
        point = coreapi.Field(
            name="point",
            location="query",
            description="Example: -122.276,45.5162",
            type="string"
            )
        fields.append(dist)
        fields.append(point)

        return fields



class SensorLocationsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Current Multnomah County Work Permits
    """

    queryset = SensorLocations.objects.all()
    serializer_class = SensorLocationsSerializer
    filter_backends = (SensorLocationsGeoFilter,)

    distance_filter_field = 'geom_4326'
    bbox_filter_include_overlapping = True # Optional
    distance_filter_convert_meters = True
