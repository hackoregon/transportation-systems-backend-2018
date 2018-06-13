
from rest_framework import serializers
from rest_framework_gis import serializers
from rest_framework.serializers import HyperlinkedRelatedField

from rest_framework.serializers import CharField

from odot_crash_api.models import Crash, CrashHr, CrashSvrty, CrashTyp, CollisTyp, Participant, Vehicle, Actn, Cause, Evnt, Err, InvstgAgy, VhclOwnshp, VhclTyp, VhclUse, WthrCond

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

class InvstgAgySerializer(serializers.ModelSerializer):

    class Meta:
        model = InvstgAgy
        fields = ('__all__')

class WthrCondSerializer(serializers.ModelSerializer):

    class Meta:
        model = WthrCond
        fields = ('__all__')

class CrashSerializer(serializers.GeoFeatureModelSerializer):
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
    invstg_agy_cd = InvstgAgySerializer()
    wthr_cond_cd = WthrCondSerializer()
    class Meta:
        model = Crash
        fields = '__all__'
        geo_field = 'geom_point'
        id = 'crash_id'

class ActnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actn
        fields = ('__all__')

class ErrSerializer(serializers.ModelSerializer):

    class Meta:
        model = Err
        fields = ('__all__')

class ParticipantSerializer(serializers.ModelSerializer):
    partic_cause_1_cd = CauseSerializer()
    partic_cause_2_cd = CauseSerializer()
    partic_cause_3_cd = CauseSerializer()
    partic_evnt_1_cd = EvntSerializer()
    partic_evnt_2_cd = EvntSerializer()
    partic_evnt_3_cd = EvntSerializer()
    partic_err_1_cd = ErrSerializer()
    partic_err_2_cd = ErrSerializer()
    partic_err_3_cd = ErrSerializer()
    crash_info = HyperlinkedRelatedField(
        read_only=True,
        view_name='crash-detail'
    )
    actn_cd = ActnSerializer()

    class Meta:
        model = Participant
        fields = '__all__'

class VhclOwnshpSerializer(serializers.ModelSerializer):

    class Meta:
        model = VhclOwnshp
        fields = ('__all__')

class VhclTypSerializer(serializers.ModelSerializer):

    class Meta:
        model = VhclTyp
        fields = ('__all__')

class VhclUseSerializer(serializers.ModelSerializer):

    class Meta:
        model = VhclUse
        fields = ('__all__')

class VehicleSerializer(serializers.ModelSerializer):
    vhcl_actn_cd = ActnSerializer()
    vhcl_cause_1_cd = CauseSerializer()
    vhcl_cause_2_cd = CauseSerializer()
    vhcl_cause_3_cd = CauseSerializer()
    vhcl_evnt_1_cd = EvntSerializer()
    vhcl_evnt_2_cd = EvntSerializer()
    vhcl_evnt_3_cd = EvntSerializer()
    vhcl_ownshp_cd = VhclOwnshpSerializer()
    vhcl_typ_cd = VhclTypSerializer()
    vhcl_use_cd = VhclUseSerializer()

    crash_info = HyperlinkedRelatedField(
        read_only=True,
        view_name='vehicle-detail'
    )

    class Meta:
        model = Vehicle
        fields = '__all__'
