
from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import CharField

from pudl_sensors_api.models import SensorLocations


class SensorLocationsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = SensorLocations
        fields = '__all__'
        geo_field = 'geom_4326'
        id = 'id'
