
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
    This viewset will provide a list of Crashes.
    """

    queryset = Crash.objects.prefetch_related("crash_severity", "crash_hour", "crash_type", "collision_type", "crash_cause_1_cd", "crash_cause_2_cd", "crash_cause_3_cd", "crash_evnt_1_cd", "crash_evnt_2_cd", "crash_evnt_3_cd", "invstg_agy_cd", "wthr_cond_cd").all()
    serializer_class = CrashSerializer

class ParticipantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Participants.
    """

    queryset = Participant.objects.prefetch_related("actn_cd",    "partic_cause_1_cd", "partic_cause_2_cd", "partic_cause_3_cd",  "partic_evnt_1_cd", "partic_evnt_2_cd",  "partic_evnt_3_cd", "partic_err_1_cd", "partic_err_2_cd", "partic_err_3_cd").all()
    serializer_class = ParticipantSerializer

class VehicleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will provide a list of Vehicles.
    """

    queryset = Vehicle.objects.prefetch_related("vhcl_actn_cd", "vhcl_cause_1_cd", "vhcl_cause_2_cd", "vhcl_cause_3_cd", "vhcl_evnt_1_cd", "vhcl_evnt_2_cd", "vhcl_evnt_3_cd",  "vhcl_use_cd", "vhcl_typ_cd", "vhcl_ownshp_cd").all()
    serializer_class = VehicleSerializer
