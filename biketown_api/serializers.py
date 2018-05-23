
from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import CharField

from biketown_api.models import BiketownTrips


class BiketownTripsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = BiketownTrips
        geo_field = "start_geom_4326"
        fields = '__all__'
