
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
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

from origin_destination_api.models import OriginDestination, ResidenceAreaCharacteristics, WorkplaceAreaCharacteristics, Xwalk
from origin_destination_api.serializers import OriginDestinationSerializer, ResidenceAreaCharacteristicsSerializer, XwalkSerializer, WorkplaceAreaCharacteristicsSerializer

class OriginDestinationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Biketown Trips.
    """

    queryset = OriginDestination.objects.all()
    serializer_class = OriginDestinationSerializer

class ResidenceAreaCharacteristicsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Biketown Trips.
    """

    queryset = ResidenceAreaCharacteristics.objects.all()
    serializer_class = ResidenceAreaCharacteristicsSerializer

class WorkplaceAreaCharacteristicsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Biketown Trips.
    """

    queryset = WorkplaceAreaCharacteristics.objects.all()
    serializer_class = WorkplaceAreaCharacteristicsSerializer

class XwalkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Biketown Trips.
    """

    queryset = Xwalk.objects.all()
    serializer_class = XwalkSerializer
