
from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import CharField

from biketown_api.models import BiketownTrips, BiketownHubs, TripCounts


class BiketownHubsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = BiketownHubs
        geo_field = 'geom_4326'
        id = "hub"
        fields = '__all__'

class BiketownTripsSerializer(serializers.ModelSerializer):
    class Meta:
        start_hub = BiketownHubsSerializer()
        end_hub = BiketownHubsSerializer()
        model = BiketownTrips
        fields = '__all__'

class TripsCountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiketownTrips
        fields = '__all__'
