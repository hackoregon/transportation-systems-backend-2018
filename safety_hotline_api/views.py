
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
import django_filters

from safety_hotline_api.models import SafetyHotlineTickets
from safety_hotline_api.serializers import SafetyHotlineTicketsSerializer

from rest_framework_gis.filters import InBBoxFilter

# class TicketFilter(FilterSet):
#     description = django_filters.CharFilter(name="description", lookup_expr='icontains')
#     class Meta:
#         model = SafetyHotlineTickets
#         fields = ['description',]


class SafetyHotlineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Safety Hotline Tickets.
    """

    queryset = SafetyHotlineTickets.objects.all()
    # filter_class = TicketFilter
    serializer_class = SafetyHotlineTicketsSerializer
