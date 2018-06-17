
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

from multco_permits_api.models import CurrentPermits, ArchivedPermits
from multco_permits_api.serializers import CurrentPermitsSerializer, ArchivedPermitsSerializer

class CurrentPermitsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Current Multnomah County Work Permits
    """

    queryset = CurrentPermits.objects.all()
    serializer_class = CurrentPermitsSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    filter_fields = '__all__'

class ArchivedPermitsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Historical Multnomah County Work Permits
    """

    queryset = ArchivedPermits.objects.all()
    serializer_class = ArchivedPermitsSerializer
    filter_backends = (SearchFilter, OrderingFilter)
