
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

from odot_crash_api.models import Crash, Participant, Vehicle
from odot_crash_api.serializers import CrashSerializer, ParticipantSerializer, VehicleSerializer

class CrashViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Biketown Trips.
    """

    queryset = Crash.objects.prefetch_related("crash_svrty_cd", "crash_hr_no", "crash_typ_cd").all()
    serializer_class = CrashSerializer

class ParticipantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Biketown Trips.
    """

    queryset = Participant.objects.prefetch_related().all()
    serializer_class = ParticipantSerializer

class VehicleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Biketown Trips.
    """

    queryset = Vehicle.objects.prefetch_related().all()
    serializer_class = VehicleSerializer
