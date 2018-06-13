
from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import CharField

from multco_permits_api.models import ArchivedPermits, CurrentPermits


class ArchivedPermitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivedPermits
        fields = '__all__'

class CurrentPermitsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = CurrentPermits
        fields = '__all__'
        geo_field = 'geom_point'
        id = 'permit_id'
