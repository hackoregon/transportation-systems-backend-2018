
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
import django_filters
from rest_framework_gis.filters import GeometryFilter
from rest_framework_gis.filterset import GeoFilterSet
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.filters import SearchFilter, OrderingFilter
import coreapi, json
import operator
from passenger_census_api.queries import getCensusTotals, getTotals, routeDetailLookup, nationalDetailLookup
from .routes import routes
from .national import national
from .service_availability import availability
from passenger_census_api.models import PassengerCensus, AnnualRouteRidership, OrCensusBlockPolygons, WaCensusBlockPolygons, AnnualCensusBlockRidership, CensusBlockChange, AnnualRouteRidership, RouteChange, AnnualRouteDifferencesForScatter
from passenger_census_api.serializers import PassengerCensusSerializer, PassengerCensusAnnualSerializer, PassengerCensusInfoSerializer, AnnualRouteRidershipSerializer, OrCensusBlockPolygonsSerializer, WaCensusBlockPolygonsSerializer, AnnualCensusBlockRidershipSerializer, CensusBlockChangeSerializer, RouteChangeSerializer, AnnualRouteDifferencesSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4000
    page_size_query_param = 'page_size'
    max_page_size = 4000

class AnnualRouteRidershipViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of individual Passenger Census counts by TRIMET.
    """

    queryset = AnnualRouteRidership.objects.all()
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filter_fields = '__all__'
    serializer_class = AnnualRouteRidershipSerializer

class AnnualRouteDifferencesViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of individual Passenger Census counts by TRIMET.
    """

    queryset = AnnualRouteDifferencesForScatter.objects.all()
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = '__all__'
    filter_fields = '__all__'
    serializer_class = AnnualRouteDifferencesSerializer

class AnnualCensusBlockRidershipViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of individual Passenger Census counts by TRIMET.
    """

    queryset = AnnualCensusBlockRidership.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    serializer_class = AnnualCensusBlockRidershipSerializer

class CensusBlockChangeViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of individual Passenger Census counts by TRIMET.
    """

    queryset = CensusBlockChange.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    serializer_class = CensusBlockChangeSerializer

class RouteChangeViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of individual Passenger Census counts by TRIMET.
    """

    queryset = RouteChange.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    serializer_class = RouteChangeSerializer

class PassengerCensusListFilter(DjangoFilterBackend):
    begin_date = django_filters.DateFilter('summary_begin_date', lookup_expr=['exact'])
    class Meta:
        model = PassengerCensus
        fields = ['begin_date']

class PassengerCensusViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of individual Passenger Census counts by TRIMET.
    """

    queryset = PassengerCensus.objects.all()
    filter_backends = (PassengerCensusListFilter,)
    serializer_class = PassengerCensusSerializer

class ServiceAvailabilityViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of total trip counts per year for Trimet.
    """
    def get_queryset(self):
        pass

    def list(self, request, *args, **kwargs):
        dictdump = json.loads(availability)
        return Response(dictdump)

class ServiceAvailabilityDetail(APIView):
    """
    This viewset will retrieve a total trip count for a given year for Trimet.
    """
    def get_object(self, pk):
        availability = availabilityDetailLookup(pk)
        return availability

    def get(self, request, pk, format=None):
        try:
            print(pk)
            availability = self.get_object(pk)
            return Response(availability)
        except:
            return Response('Year Not Found', status=status.HTTP_404_NOT_FOUND)

class NationalTotalsViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of annual national transporation ridership counts based on Transit Report's report: http://tram.mcgill.ca/Research/Publications/Transit_Ridership_overtime.pdf.
    """
    def get_queryset(self):
        pass

    def list(self, request, *args, **kwargs):
        dictdump = json.loads(national)
        return Response(dictdump)

class NationalDetail(APIView):
    """
    This viewset returns a specific year's national ridership count based on Transit Report's report: http://tram.mcgill.ca/Research/Publications/Transit_Ridership_overtime.pdf.
    """
    def get_object(self, pk):

        national = nationalDetailLookup(pk)
        return national

    def get(self, request, pk, format=None):
        try:
            national = self.get_object(pk)
            print(pk)
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
    This viewset will provide a specific route.
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

class PassengerCensusAnnualBussesAvgViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a info about Annual System Wide Avgs for bus routes.
    """
    serializer_class = PassengerCensusInfoSerializer

    def list(self, request, *args, **kwargs):
        census = PassengerCensus.objects.filter(route_number__in=["1", "2", "4", "4", "6", "8", "9", "10", "11", "12", "14", "15", "16", "17", "18", "19", "20", "20", "21", "22", "23", "24", "25", "29", "30", "32", "33", "34", "35", "36", "37", "38", "39", "42", "43", "44", "45", "46", "47", "48", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "61", "62", "63", "64", "65", "66", "67", "68", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "84", "85", "87", "88", "90", "92", "93", "94", "96", "97", "99", "152", "154", "155", "156", "203", "272", "291"])
        weekly = getTotals(census)
        return Response(weekly)

class PassengerCensusAnnualTrainsAvgViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a info about Annual System Wide Avgs for the Max and WES Commuter Lines
    """
    serializer_class = PassengerCensusInfoSerializer

    def list(self, request, *args, **kwargs):
        census = PassengerCensus.objects.filter(route_number__in=[
          "100",
          "190",
          "203",
          "200",
          "290"
        ])
        weekly = getTotals(census)
        return Response(weekly)

class PassengerCensusAnnualStreetCarAvgViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a info about Annual System Wide Avgs for the Portland Street Car
    """
    serializer_class = PassengerCensusInfoSerializer

    def list(self, request, *args, **kwargs):
        census = PassengerCensus.objects.filter(route_number__in=[
          "193",
          "194",
          "195"
        ])
        weekly = getTotals(census)
        return Response(weekly)

class PassengerCensusAnnualTramAvgViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a info about Annual System Wide Avgs for the Portland Aerial Tram
    """
    serializer_class = PassengerCensusInfoSerializer

    def list(self, request, *args, **kwargs):
        census = PassengerCensus.objects.filter(route_number__in=[
          "208"
        ])
        weekly = getTotals(census)
        return Response(weekly)

class PassengerCensusAnnualSystemAvgViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a info about Annual System Wide Avgs.
    """
    serializer_class = PassengerCensusInfoSerializer

    def list(self, request, *args, **kwargs):
        census = PassengerCensus.objects.all()
        weekly = getTotals(census)
        return Response(weekly)

class PassengerCensusAnnualSystemTotalViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset is deprecated. Returns same values as `/system/annual/average`. Please update to use other endpoint
    """
    serializer_class = PassengerCensusInfoSerializer

    def list(self, request, *args, **kwargs):
        census = PassengerCensus.objects.all()
        weekly = getTotals(census)
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

class PassengerCensusRoutesAnnualTotalViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset is deprecated. Pleae use the `/routes/annual/averages` endpoint which returns same values
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

class PassengerCensusRoutesAnnualAvgViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of Passenger Census by Routes calculated for an yearly average.
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

class OrCensusBlockPolygonsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will return GeoJson for Census Blocks in Portland Metro Area within Oregon
    """
    queryset = OrCensusBlockPolygons.objects.all()
    serializer_class = OrCensusBlockPolygonsSerializer

class WaCensusBlockPolygonsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset will return GeoJson for Census Blocks in Portland Metro Area within Washington
    """

    queryset = WaCensusBlockPolygons.objects.all()
    serializer_class = WaCensusBlockPolygonsSerializer
