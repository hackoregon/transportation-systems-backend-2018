
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Count
from django.db.models.functions import ExtractYear
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rest_framework import generics, permissions, renderers, viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.pagination import PageNumberPagination

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
import coreapi, json
import operator



from passenger_census_api.models import PassengerCensus
from passenger_census_api.serializers import PassengerCensusSerializer, PassengerCensusRoutesSerializer, PassengerCensusAnnualSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4000
    page_size_query_param = 'page_size'
    max_page_size = 4000


class PassengerCensusViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of Passenger Census.
    """

    queryset = PassengerCensus.objects.all()
    serializer_class = PassengerCensusSerializer

class PassengerCensusRoutesViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of Passenger Census.
    """

    queryset = PassengerCensus.objects.order_by('route_number').values('route_number').distinct()
    serializer_class = PassengerCensusRoutesSerializer
    pagination_class = LargeResultsSetPagination

class PassengerCensusRetrieveViewSet(viewsets.ViewSetMixin, generics.RetrieveAPIView):
    """
    This viewset allows you to retrieve a specific Passenger Census entry based on an ID.
    """

    queryset = PassengerCensus.objects.all()
    serializer_class = PassengerCensusSerializer

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
            )
        fields.append(year)
        fields.append(route)

        return fields

class PassengerCensusRoutesAnnualViewSet(viewsets.ViewSetMixin, generics.ListAPIView):
    """
    This viewset will provide a list of Passenger Census by Routes in annual summary.
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
                        annuals = stops.values(year=ExtractYear("summary_begin_date")).annotate(
                            num_of_yearly_census=Count('summary_begin_date', distinct=True)).order_by("year")
                        weekly = stops.filter(service_key__icontains="W").values(year=ExtractYear("summary_begin_date")).annotate(
                            weekday_sum_ons=Sum('ons')*5*52/Count('summary_begin_date', distinct=True),
                            weekday_sum_offs=Sum('offs')*5*52/Count('summary_begin_date', distinct=True),
                            weekday_total_stops=Count('ons')*5*52/Count('summary_begin_date', distinct=True),
                            ).order_by("year")
                        saturday = stops.filter(service_key__icontains="S").values(year=ExtractYear("summary_begin_date")).annotate(
                            saturday_sum_ons=Sum('ons')*52/Count('summary_begin_date', distinct=True),
                            saturday_sum_offs=Sum('offs')*52/Count('summary_begin_date', distinct=True),
                            saturday_total_stops=Count('ons')*5*52/Count('summary_begin_date', distinct=True)).order_by("year")
                        sunday = stops.filter(service_key__icontains="U").values(year=ExtractYear("summary_begin_date")).annotate(
                            sunday_sum_ons=Sum('ons')*52/Count('summary_begin_date', distinct=True),
                            sunday_sum_offs=Sum('offs')*52/Count('summary_begin_date', distinct=True),
                            sunday_total_stops=Count('ons')*5*52/Count('summary_begin_date', distinct=True)).order_by("year")
                        sorting_key = operator.itemgetter("year")
                        for i, j in zip(sorted(weekly, key=sorting_key), sorted(saturday, key=sorting_key)):i.update(j)
                        for i, j in zip(sorted(weekly, key=sorting_key), sorted(sunday, key=sorting_key)):i.update(j)
                        for i, j in zip(sorted(weekly, key=sorting_key), sorted(annuals, key=sorting_key)):i.update(j)
                        for week in weekly:
                            week["sunday_census"] = True
                            week["saturday_census"] = True
                            if  "saturday_sum_ons" not in week:
                                week["saturday_sum_ons"] = 0
                                week["saturday_sum_offs"]  = 0
                                week["saturday_total_stops"] = 0
                                week["saturday_census"] = False
                            if "sunday_sum_ons" not in week:
                                week["sunday_sum_ons"] = 0
                                week["sunday_sum_offs"]  = 0
                                week["sunday_total_stops"] = 0
                                week["sunday_census"] = False
                            week["annual_sum_ons"] = week["weekday_sum_ons"] + week["saturday_sum_ons"] + week["sunday_sum_ons"]
                            week["annual_sum_offs"] = week["weekday_sum_offs"] + week["saturday_sum_offs"] + week["sunday_sum_offs"]
                            week["total_annual_stops"] = week["weekday_total_stops"] + week["saturday_total_stops"] + week["sunday_total_stops"]
                        return Response(weekly)
                        # return Response(annuals)
                else:
                    return Response('Route Number not found', status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response('Route Number must be integer', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Missing Route Number paramater', status=status.HTTP_400_BAD_REQUEST)


    # filter_fields = ['route_number',]
