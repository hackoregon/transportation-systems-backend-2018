from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from . import models

class SafetyHotlineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.SafetyHotlineTickets
        fields = ('date_created', 'description')
        geo_field = "geom_4326"