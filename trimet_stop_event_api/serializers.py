
from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import CharField

from trimet_stop_event_api.models import TrimetStopEvents, TotalsOnsByHour, DisturbanceStops


class DisturbanceStopsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = DisturbanceStops
        fields = '__all__'
        geo_field = 'geom_4326'
        id = 'id'

class TrimetStopEventsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = TrimetStopEvents
        fields = '__all__'
        geo_field = 'geom_point_4326'
        id = 'id'

class TotalsOnsByHourSerializer(serializers.ModelSerializer):
    model = TotalsOnsByHour
    fields = '__all__'
