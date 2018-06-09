
from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import CharField, IntegerField

from passenger_census_api.models import PassengerCensus


class PassengerCensusSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = PassengerCensus
        geo_field = "geom_4326"
        id = 'id'
        fields = '__all__'

class PassengerCensusRoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerCensus
        fields = ['route_number',]

class PassengerCensusAnnualSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerCensus
        fields = '__all__'
        year = IntegerField()
