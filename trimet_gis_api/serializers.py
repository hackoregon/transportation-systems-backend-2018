
from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import CharField


from trimet_gis_api.models import TmBoundary, TmParkride


class TmBoundarySerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = TmBoundary
        geo_field = "wkb_geometry"
        fields = '__all__'

class TmParkrideSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = TmParkride
        geo_field = "wkb_geometry"
        fields = '__all__'
