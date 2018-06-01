
from rest_framework import serializers
# from rest_framework_gis import serializers
from rest_framework.serializers import CharField

from odot_crash_api.models import Crash, CrashHr, CrashSvrty, CrashTyp, CollisTyp, Participant, Vehicle, Actn, Cause, Evnt

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

class CollisTypSerializer(serializers.ModelSerializer):

    class Meta:
        model = CollisTyp
        fields = ('__all__')

class CauseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cause
        fields = ('__all__')

class EvntSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evnt
        fields = ('__all__')

class CrashSerializer(serializers.ModelSerializer):
    crash_hour = CrashHrSerializer()
    crash_severity = CrashSvrtySerializer()
    crash_type = CrashTypSerializer()
    collision_type = CollisTypSerializer()
    crash_cause_1_cd = CauseSerializer()
    crash_cause_2_cd = CauseSerializer()
    crash_cause_3_cd = CauseSerializer()
    crash_evnt_1_cd = EvntSerializer()
    crash_evnt_2_cd = EvntSerializer()
    crash_evnt_3_cd = EvntSerializer()
    class Meta:
        model = Crash
        fields = '__all__'

class ActnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actn
        fields = ('__all__')

class ParticipantSerializer(serializers.ModelSerializer):
    crash_info = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='crash-detail'
    )
    actn_cd = ActnSerializer()

    class Meta:
        model = Participant
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    crash_info = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='vehicle-detail'
    )

    class Meta:
        model = Vehicle
        fields = '__all__'
