
from rest_framework import serializers
# from rest_framework_gis import serializers
from rest_framework.serializers import CharField

from odot_crash_api.models import Crash, CrashHr, CrashSvrty, CrashTyp, Participant, Vehicle

class CrashHrSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrashHr
        fields = ('__all__')

class CrashSvrtySerializer(serializers.ModelSerializer):

    class Meta:
        model = CrashSvrty
        fields = ('__all__')

class CrashTypSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrashTyp
        fields = ('__all__')

class CrashSerializer(serializers.ModelSerializer):
    crash_hr_no = CrashHrSerializer()
    crash_svrty_cd = CrashSvrtySerializer()
    crash_typ_cd = CrashTypSerializer()
    class Meta:
        model = Crash
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    crash_id = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='crash-detail'
    )

    class Meta:
        model = Participant
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    crash_id = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='vehicle-detail'
    )

    class Meta:
        model = Vehicle
        fields = '__all__'
