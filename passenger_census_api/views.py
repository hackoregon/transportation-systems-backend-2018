
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rest_framework import generics, permissions, renderers, viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.pagination import PageNumberPagination

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
import coreapi


from passenger_census_api.models import PassengerCensus
from passenger_census_api.serializers import PassengerCensusSerializer, PassengerCensusRoutesSerializer


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

    queryset = PassengerCensus.objects.all()
    serializer_class = PassengerCensusSerializer
    filter_backends = (PassengerCensusDateFilter,)
    pagination_class = LargeResultsSetPagination

    def list(self, request, *args, **kwargs):
        if request.GET.get('route', ' ') != ' ':
            this_route_number = request.GET.get('route', ' ')
            try:
                stops = PassengerCensus.objects.filter(route_number=this_route_number)
                if stops:
                    if request.GET.get('year', ' ') != ' ':
                        this_year = request.GET.get('year', ' ')
                        try:
                            stops = stops.filter(summary_begin_date__year=this_year)
                            if stops:
                                annual_sums = stops.aggregate(sum_ons=Sum('ons')*26, sum_offs=Sum('offs')*26)
                                weekday_sums = stops.filter(service_key__icontains="W").aggregate(sum_ons=Sum('ons')*5*26, sum_offs=Sum('offs')*5*26)
                                saturday_sums = stops.filter(service_key__icontains="S").aggregate(sum_ons=Sum('ons')*26, sum_offs=Sum('offs')*26)
                                sunday_sums = stops.filter(service_key__icontains="U").aggregate(sum_ons=Sum('ons')*26, sum_offs=Sum('offs')*26)
                                serialized_stops = PassengerCensusSerializer(stops, many=True)
                                return Response({'route_number': this_route_number,
                                    'year': this_year,
                                    'total_stops': stops.count(),
                                    'annual_sums': annual_sums,
                                    'weekday_sums': weekday_sums,
                                    'saturday_sums': saturday_sums,
                                    'sunday_sums': sunday_sums
                                    })
                            else:
                                return Response('No Data found for Route Number and Year', status=status.HTTP_404_NOT_FOUND)
                        except ValueError:
                            return Response('Search year must be four digit year', status=status.HTTP_400_BAD_REQUEST)
                    else:
                        if stops:
                            annual_sums = stops.aggregate(sum_ons=Sum('ons')*26, sum_offs=Sum('offs')*26)
                            weekday_sums = stops.filter(service_key__icontains="W").aggregate(sum_ons=Sum('ons')*5, sum_offs=Sum('offs')*5)
                            saturday_sums = stops.filter(service_key__icontains="S").aggregate(sum_ons=Sum('ons')*26, sum_offs=Sum('offs')*26)
                            sunday_sums = stops.filter(service_key__icontains="U").aggregate(sum_ons=Sum('ons')*26, sum_offs=Sum('offs')*26)
                            serialized_stops = PassengerCensusSerializer(stops, many=True)
                            return Response({'route_number': this_route_number,
                                'total_stops': stops.count(),
                                'annual_sums': annual_sums,
                                'weekday_sums': weekday_sums,
                                'saturday_sums': saturday_sums,
                                'sunday_sums': sunday_sums
                                })
                else:
                    return Response('Route Number not found', status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response('Route Number must be integer', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Missing Route Number paramater', status=status.HTTP_400_BAD_REQUEST)


    # filter_fields = ['route_number',]
