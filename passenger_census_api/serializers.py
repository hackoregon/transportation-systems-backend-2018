
from rest_framework import serializers
from rest_framework_gis import serializers

from rest_framework.serializers import CharField, IntegerField, BooleanField

from passenger_census_api.models import PassengerCensus


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
