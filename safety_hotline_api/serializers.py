
from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import CharField

from safety_hotline_api.models import SafetyHotlineTickets


class SafetyHotlineTicketsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = SafetyHotlineTickets
        geo_field = "geom_4326"
        fields = '__all__'
