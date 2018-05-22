
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

from biketown_api.models import BiketownTrips
from biketown_api.serializers import BiketownTripsSerializer

class BiketownTripsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Biketown Trips.
    """

    queryset = BiketownTrips.objects.all()
    serializer_class = BiketownTripsSerializer
    # filter_backends = (SearchFilter,DjangoFilterBackend,OrderingFilter,)
    # search_fields = '__all__'
    # filter_fields = '__all__'
    # ordering_fields = '__all__'

    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = {'gid': ['exact',],
    #         'fma': ['exact',],
    #         }
