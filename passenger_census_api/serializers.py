
from rest_framework import serializers
from rest_framework_gis import serializers

from rest_framework.serializers import CharField, IntegerField, BooleanField

from passenger_census_api.models import PassengerCensus, AnnualRouteRidership, OrCensusBlockPolygons, WaCensusBlockPolygons, AnnualCensusBlockRidership, CensusBlockChange, RouteChange

class AnnualCensusBlockRidershipSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = AnnualCensusBlockRidership
        fields = '__all__'
        geo_field = 'geom_polygon_4326'


class AnnualRouteRidershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualRouteRidership
        fields = '__all__'

class CensusBlockChangeSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = CensusBlockChange
        fields = '__all__'
        geo_field = 'geom_polygon_4326'

class RouteChangeSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = RouteChange
        fields = '__all__'
        geo_field = 'geom_linestring'

class OrCensusBlockPolygonsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = OrCensusBlockPolygons
        geo_field = 'geom_polygon_4326'
        id = 'census_block'
        fields = '__all__'

class WaCensusBlockPolygonsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = WaCensusBlockPolygons
        geo_field = 'geom_polygon_4326'
        id = 'census_block'
        fields = '__all__'

class PassengerCensusSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = PassengerCensus
        geo_field = 'geom_4326'
        id = 'id'
        fields = '__all__'

class PassengerCensusAnnualSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerCensus
        year = IntegerField()
        weekday_sum_ons = IntegerField()
        weekday_sum_offs = IntegerField()
        saturday_sum_ons = IntegerField()
        saturday_sum_offs = IntegerField()
        num_of_yearly_census = IntegerField()
        sunday_census = BooleanField()
        saturday_census = BooleanField()
        sunday_sum_ons = IntegerField()
        sunday_sum_offs = IntegerField()
        annual_sum_ons = IntegerField()
        annual_sum_offs = IntegerField()

class PassengerCensusInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerCensus
        fields = ['summary_begin_date', 'service_key']
        total_routes = IntegerField()
