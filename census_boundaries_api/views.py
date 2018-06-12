
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

from census_boundaries_api.models import Tl201741Tabblock10, Tl201753Tabblock10
from census_boundaries_api.serializers import Tl201741Tabblock10Serializer, Tl201753Tabblock10Serializer

class Tl201741Tabblock10ViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Biketown Trips.
    """

    queryset = Tl201741Tabblock10.objects.all()
    serializer_class = Tl201741Tabblock10Serializer

class Tl201753Tabblock10ViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Biketown Trips.
    """

    queryset = Tl201753Tabblock10.objects.all()
    serializer_class = Tl201753Tabblock10Serializer
