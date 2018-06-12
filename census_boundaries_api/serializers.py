
from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import CharField

from census_boundaries_api.models import Tl201741Tabblock10, Tl201753Tabblock10


class Tl201741Tabblock10Serializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Tl201741Tabblock10
        fields = '__all__'
        geo_field = 'wkb_geometry'
        id = 'ogc_fid'

class Tl201753Tabblock10Serializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Tl201753Tabblock10
        fields = '__all__'
        geo_field = 'wkb_geometry'
        id = 'ogc_fid'
