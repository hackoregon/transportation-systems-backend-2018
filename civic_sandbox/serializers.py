from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from . import models

class SafetyHotlineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.SafetyHotlineTickets
        fields = '__all__'
        geo_field = 'geom_4326'

class CrashSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Crash
        fields = '__all__'
        geo_field = 'geom_point'