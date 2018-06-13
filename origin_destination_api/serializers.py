
from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import CharField

from origin_destination_api.models import OriginDestination, ResidenceAreaCharacteristics, WorkplaceAreaCharacteristics, Xwalk

class OriginDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginDestination
        fields = '__all__'

class ResidenceAreaCharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidenceAreaCharacteristics
        fields = '__all__'


class WorkplaceAreaCharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkplaceAreaCharacteristics
        fields = '__all__'
#
class XwalkSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Xwalk
        fields = '__all__'
        geo_field = 'geom_intpt_4326'
        id = 'tabblk2010'
