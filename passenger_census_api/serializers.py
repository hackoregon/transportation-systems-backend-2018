
from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import CharField

from passenger_census_api.models import PassengerCensus


class PassengerCensusSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = PassengerCensus
        geo_field = "geom_2913"
        id = 'id'
        fields = '__all__'

class PassengerCensusRoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerCensus
        fields = ['route_number',]
