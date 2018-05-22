
from rest_framework import serializers
from rest_framework.serializers import CharField

from trimet_stop_event_api.models import TrimetStopEvents


class TrimetStopEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrimetStopEvents
        fields = '__all__'
