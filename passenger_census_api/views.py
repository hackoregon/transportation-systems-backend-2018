
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Count, Case, When, Value, CharField
from django.db.models.functions import ExtractYear
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rest_framework import generics, permissions, renderers, viewsets, status, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.pagination import PageNumberPagination

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
import coreapi, json
import operator
from passenger_census_api.queries import getAvgs, getCensusTotals, getTotals, routeDetailLookup
from .routes import routes
from .national import national


from passenger_census_api.models import PassengerCensus, AnnualRouteRidership, OrCensusBlockPolygons, WaCensusBlockPolygons
from passenger_census_api.serializers import PassengerCensusSerializer, PassengerCensusAnnualSerializer, PassengerCensusInfoSerializer, AnnualRouteRidershipSerializer, OrCensusBlockPolygonsSerializer, WaCensusBlockPolygonsSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4000
    page_size_query_param = 'page_size'
    max_page_size = 4000


class PassengerCensusViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of individual Passenger Census by TRIMET.
    """

    queryset = PassengerCensus.objects.all()
    serializer_class = PassengerCensusSerializer

class NationalTotalsViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of distinct routes in the Passenger Census by TRIMET.
    """
    def get_queryset(self):
        pass

    def list(self, request, *args, **kwargs):
        dictdump = json.loads(national)
        return Response(dictdump)

class NationalDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):

        national = nationalDetailLookup(pk)
        return national

    def get(self, request, pk, format=None):
        try:
            national = self.get_object(pk)
            return Response(national)
        except:
            return Response('Year Not Found', status=status.HTTP_404_NOT_FOUND)

class PassengerCensusRoutesViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of distinct routes in the Passenger Census by TRIMET.
    """
    def get_queryset(self):
        pass

    def list(self, request, *args, **kwargs):
        dictdump = json.loads(routes)
        return Response(dictdump)

class RouteDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):

        route = routeDetailLookup(pk)
        return route

    def get(self, request, pk, format=None):
        try:
            route = self.get_object(pk)
            return Response(route)
        except:
            return Response('Route Number not found', status=status.HTTP_404_NOT_FOUND)

class PassengerCensusRetrieveViewSet(viewsets.ViewSetMixin, generics.RetrieveAPIView):
    """
    This viewset allows you to retrieve a specific Passenger Census entry based on an ID.
    """

    queryset = PassengerCensus.objects.all()
    serializer_class = PassengerCensusSerializer

class PassengerCensusInfoViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a info about the Passenger Census by TRIMET.

    Returns:
    Distinct Census Dates
    The total number of routes for the census
    The total number of stops for the census
    """
    serializer_class = PassengerCensusInfoSerializer

    def list(self, request, *args, **kwargs):
        census = PassengerCensus.objects.all()
        census = getCensusTotals(census)
        return Response(census)

class PassengerCensusAnnualSystemTotalViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a info about Annual System Wide Totals.
    """
    serializer_class = PassengerCensusInfoSerializer

    def list(self, request, *args, **kwargs):
        census = PassengerCensus.objects.all()
        weekly = getTotals(census)
        return Response(weekly)

class PassengerCensusAnnualSystemAvgViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a info about Annual System Wide Totals.
    """
    serializer_class = PassengerCensusInfoSerializer

    def list(self, request, *args, **kwargs):
        census = PassengerCensus.objects.all()
        weekly = getAvgs(census)
        return Response(weekly)

class PassengerCensusDateFilter(DjangoFilterBackend):
    """
    This filter is used to inject custom filter fields into schema.
    """

    class Meta:
        model = PassengerCensus
        fields = []

    def get_schema_fields(self, view):
        fields = []
        year = coreapi.Field(
            name="year",
            location="query",
            description="YYYY",
            type="number",
            )
        route = coreapi.Field(
            name="route",
            location="query",
            description="route number",
            type="number",
            required="true"
            )
        fields.append(year)
        fields.append(route)

        return fields

class PassengerCensusRoutesAnnualAvgViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of Passenger Census by Routes calculated for a total year.
    """

    # queryset = PassengerCensus.objects.all()
    serializer_class = PassengerCensusAnnualSerializer
    filter_backends = (PassengerCensusDateFilter,)
    pagination_class = LargeResultsSetPagination

    def list(self, request, *args, **kwargs):
        if request.GET.get('route', ' ') != ' ':
            this_route_number = request.GET.get('route', ' ')
            try:
                stops = PassengerCensus.objects.filter(route_number=this_route_number)
                if stops.exists():
                    if request.GET.get('year', ' ') != ' ':
                        this_year = request.GET.get('year', ' ')
                        try:
                            stops = stops.filter(summary_begin_date__year=this_year)
                        except ValueError:
                            return Response('Search year must be four digit year', status=status.HTTP_400_BAD_REQUEST)
                    if stops.exists():
                        weekly = getAvgs(stops)
                        return Response(weekly)
                else:
                    return Response('Route Number not found', status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response('Route Number must be integer', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Missing Route Number paramater', status=status.HTTP_400_BAD_REQUEST)

class PassengerCensusRoutesAnnualTotalViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of Passenger Census by Routes calculated for a total year.
    """

    # queryset = PassengerCensus.objects.all()
    serializer_class = PassengerCensusAnnualSerializer
    filter_backends = (PassengerCensusDateFilter,)
    pagination_class = LargeResultsSetPagination

    def list(self, request, *args, **kwargs):
        if request.GET.get('route', ' ') != ' ':
            this_route_number = request.GET.get('route', ' ')

            try:
                stops = PassengerCensus.objects.filter(route_number=this_route_number)
                if stops.exists():
                    if request.GET.get('year', ' ') != ' ':
                        this_year = request.GET.get('year', ' ')
                        try:
                            stops = stops.filter(summary_begin_date__year=this_year)
                        except ValueError:
                            return Response('Search year must be four digit year', status=status.HTTP_400_BAD_REQUEST)
                    if stops.exists():
                        weekly = getTotals(stops)
                        return Response(weekly)
                else:
                    return Response('Route Number not found', status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response('Route Number must be integer', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Missing Route Number paramater', status=status.HTTP_400_BAD_REQUEST)

    # filter_fields = ['route_number',]

class PassengerCensusAnnualRollupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnnualRouteRidership.objects.all()
    serializer_class = AnnualRouteRidershipSerializer

class OrCensusBlockPolygonsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrCensusBlockPolygons.objects.all()
    serializer_class = OrCensusBlockPolygonsSerializer

class WaCensusBlockPolygonsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WaCensusBlockPolygons.objects.all()
    serializer_class = WaCensusBlockPolygonsSerializer
