
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

from passenger_census_api.models import PassengerCensus
from passenger_census_api.serializers import PassengerCensusSerializer

class PassengerCensusViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Passenger Census.
    """

    queryset = PassengerCensus.objects.all()
    serializer_class = PassengerCensusSerializer
    # filter_backends = (SearchFilter,DjangoFilterBackend,OrderingFilter,)
    # search_fields = '__all__'
    # filter_fields = '__all__'
    # ordering_fields = '__all__'

    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = {'gid': ['exact',],
    #         'fma': ['exact',],
    #         }
