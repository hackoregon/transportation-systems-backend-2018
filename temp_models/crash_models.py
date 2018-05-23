# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actn(models.Model):
    actn_cd = models.IntegerField(blank=True, null=True)
    actn_long_desc = models.TextField(blank=True, null=True)
    actn_med_desc = models.TextField(blank=True, null=True)
    actn_short_desc = models.TextField(blank=True, null=True)
    actn_partic_valid_flg = models.IntegerField(blank=True, null=True)
    actn_vhcl_valid_flg = models.IntegerField(blank=True, null=True)
    actn_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actn'


class Cause(models.Model):
    cause_cd = models.IntegerField(blank=True, null=True)
    cause_long_desc = models.TextField(blank=True, null=True)
    cause_med_desc = models.TextField(blank=True, null=True)
    cause_short_desc = models.TextField(blank=True, null=True)
    cause_crash_valid_flg = models.IntegerField(blank=True, null=True)
    cause_partic_valid_flg = models.IntegerField(blank=True, null=True)
    cause_vhcl_valid_flg = models.IntegerField(blank=True, null=True)
    cause_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cause'


class CityFipsHist(models.Model):
    city_sect_id = models.IntegerField(blank=True, null=True)
    city_fips_hist_start_yr_no = models.IntegerField(blank=True, null=True)
    city_fips_hist_termnt_yr_no = models.IntegerField(blank=True, null=True)
    fips_city_id = models.IntegerField(blank=True, null=True)
    city_sect_urb_rural_area_ind = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city_fips_hist'


class CitySect(models.Model):
    city_sect_id = models.IntegerField(blank=True, null=True)
    city_sect_nm = models.TextField(blank=True, null=True)
    city_sect_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city_sect'


class CmpssDrct(models.Model):
    cmpss_dir_cd = models.IntegerField(blank=True, null=True)
    cmpss_dir_short_desc = models.TextField(blank=True, null=True)
    cmpss_dir_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmpss_drct'


class Cnty(models.Model):
    cnty_id = models.IntegerField(blank=True, null=True)
    cnty_nm = models.TextField(blank=True, null=True)
    fips_cnty_id = models.IntegerField(blank=True, null=True)
    cnty_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cnty'


class CollisTyp(models.Model):
    collis_typ_cd = models.TextField(blank=True, null=True)
    collis_typ_long_desc = models.TextField(blank=True, null=True)
    collis_typ_alt_long_desc = models.TextField(blank=True, null=True)
    collis_typ_med_desc = models.TextField(blank=True, null=True)
    collis_typ_short_desc = models.TextField(blank=True, null=True)
    collis_typ_sort_ordr_no = models.IntegerField(blank=True, null=True)
    collis_typ_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collis_typ'


class Crash(models.Model):
    crash_id = models.IntegerField(primary_key=True)
    ser_no = models.TextField(blank=True, null=True)
    crash_dt = models.TextField(blank=True, null=True)
    crash_mo_no = models.IntegerField(blank=True, null=True)
    crash_day_no = models.IntegerField(blank=True, null=True)
    crash_yr_no = models.IntegerField(blank=True, null=True)
    crash_wk_day_cd = models.IntegerField(blank=True, null=True)
    crash_hr_no = models.IntegerField(blank=True, null=True)
    crash_hr_short_desc = models.TextField(blank=True, null=True)
    cnty_id = models.IntegerField(blank=True, null=True)
    cnty_nm = models.TextField(blank=True, null=True)
    city_sect_id = models.IntegerField(blank=True, null=True)
    city_sect_nm = models.TextField(blank=True, null=True)
    urb_area_cd = models.IntegerField(blank=True, null=True)
    urb_area_short_nm = models.TextField(blank=True, null=True)
    fc_cd = models.IntegerField(blank=True, null=True)
    fc_short_desc = models.TextField(blank=True, null=True)
    nhs_flg = models.IntegerField(blank=True, null=True)
    hwy_no = models.IntegerField(blank=True, null=True)
    hwy_sfx_no = models.NullBooleanField()
    hwy_med_nm = models.TextField(blank=True, null=True)
    rdwy_no = models.IntegerField(blank=True, null=True)
    hwy_compnt_cd = models.IntegerField(blank=True, null=True)
    hwy_compnt_short_desc = models.TextField(blank=True, null=True)
    mlge_typ_cd = models.IntegerField(blank=True, null=True)
    mlge_typ_short_desc = models.TextField(blank=True, null=True)
    rd_con_no = models.IntegerField(blank=True, null=True)
    lrs_val = models.TextField(blank=True, null=True)
    lat_deg_no = models.IntegerField(blank=True, null=True)
    lat_minute_no = models.IntegerField(blank=True, null=True)
    lat_sec_no = models.FloatField(blank=True, null=True)
    longtd_deg_no = models.IntegerField(blank=True, null=True)
    longtd_minute_no = models.IntegerField(blank=True, null=True)
    longtd_sec_no = models.FloatField(blank=True, null=True)
    lat_dd = models.FloatField(blank=True, null=True)
    longtd_dd = models.FloatField(blank=True, null=True)
    specl_jrsdct_id = models.NullBooleanField()
    specl_jrsdct_short_desc = models.NullBooleanField()
    jrsdct_grp_cd = models.NullBooleanField()
    jrsdct_grp_long_desc = models.NullBooleanField()
    agy_st_no = models.TextField(blank=True, null=True)
    st_full_nm = models.TextField(blank=True, null=True)
    recre_rd_nm = models.NullBooleanField()
    isect_agy_st_no = models.TextField(blank=True, null=True)
    isect_st_full_nm = models.TextField(blank=True, null=True)
    isect_recre_rd_nm = models.NullBooleanField()
    isect_seq_no = models.IntegerField(blank=True, null=True)
    from_isect_dstnc_qty = models.IntegerField(blank=True, null=True)
    cmpss_dir_cd = models.IntegerField(blank=True, null=True)
    mp_no = models.FloatField(blank=True, null=True)
    post_speed_lmt_val = models.IntegerField(blank=True, null=True)
    rd_char_cd = models.IntegerField(blank=True, null=True)
    rd_char_short_desc = models.TextField(blank=True, null=True)
    off_rdwy_flg = models.IntegerField(blank=True, null=True)
    isect_typ_cd = models.IntegerField(blank=True, null=True)
    isect_typ_short_desc = models.TextField(blank=True, null=True)
    isect_rel_flg = models.IntegerField(blank=True, null=True)
    rndabt_flg = models.IntegerField(blank=True, null=True)
    drvwy_rel_flg = models.IntegerField(blank=True, null=True)
    ln_qty = models.IntegerField(blank=True, null=True)
    turng_leg_qty = models.IntegerField(blank=True, null=True)
    medn_typ_cd = models.IntegerField(blank=True, null=True)
    medn_typ_short_desc = models.TextField(blank=True, null=True)
    impct_loc_cd = models.IntegerField(blank=True, null=True)
    crash_typ_cd = models.TextField(blank=True, null=True)
    crash_typ_short_desc = models.TextField(blank=True, null=True)
    collis_typ_cd = models.TextField(blank=True, null=True)
    collis_typ_short_desc = models.TextField(blank=True, null=True)
    crash_svrty_cd = models.IntegerField(blank=True, null=True)
    crash_svrty_short_desc = models.TextField(blank=True, null=True)
    wthr_cond_cd = models.IntegerField(blank=True, null=True)
    wthr_cond_short_desc = models.TextField(blank=True, null=True)
    rd_surf_cond_cd = models.IntegerField(blank=True, null=True)
    rd_surf_short_desc = models.TextField(blank=True, null=True)
    lgt_cond_cd = models.IntegerField(blank=True, null=True)
    lgt_cond_short_desc = models.TextField(blank=True, null=True)
    traf_cntl_device_cd = models.IntegerField(blank=True, null=True)
    traf_cntl_device_short_desc = models.TextField(blank=True, null=True)
    traf_cntl_func_flg = models.IntegerField(blank=True, null=True)
    invstg_agy_cd = models.IntegerField(blank=True, null=True)
    invstg_agy_short_desc = models.TextField(blank=True, null=True)
    crash_evnt_1_cd = models.IntegerField(blank=True, null=True)
    crash_evnt_1_short_desc = models.TextField(blank=True, null=True)
    crash_evnt_2_cd = models.IntegerField(blank=True, null=True)
    crash_evnt_2_short_desc = models.TextField(blank=True, null=True)
    crash_evnt_3_cd = models.IntegerField(blank=True, null=True)
    crash_evnt_3_short_desc = models.TextField(blank=True, null=True)
    crash_cause_1_cd = models.IntegerField(blank=True, null=True)
    crash_cause_1_short_desc = models.TextField(blank=True, null=True)
    crash_cause_2_cd = models.IntegerField(blank=True, null=True)
    crash_cause_2_short_desc = models.TextField(blank=True, null=True)
    crash_cause_3_cd = models.IntegerField(blank=True, null=True)
    crash_cause_3_short_desc = models.TextField(blank=True, null=True)
    schl_zone_ind = models.IntegerField(blank=True, null=True)
    wrk_zone_ind = models.IntegerField(blank=True, null=True)
    alchl_invlv_flg = models.IntegerField(blank=True, null=True)
    drug_invlv_flg = models.IntegerField(blank=True, null=True)
    crash_speed_invlv_flg = models.IntegerField(blank=True, null=True)
    crash_hit_run_flg = models.IntegerField(blank=True, null=True)
    pop_rng_cd = models.IntegerField(blank=True, null=True)
    pop_rng_med_desc = models.TextField(blank=True, null=True)
    rd_cntl_cd = models.IntegerField(blank=True, null=True)
    rd_cntl_med_desc = models.TextField(blank=True, null=True)
    rte_typ_cd = models.TextField(blank=True, null=True)
    rte_id = models.TextField(blank=True, null=True)
    rte_nm = models.TextField(blank=True, null=True)
    reg_id = models.IntegerField(blank=True, null=True)
    dist_id = models.TextField(blank=True, null=True)
    seg_mrk_id = models.TextField(blank=True, null=True)
    seg_pt_lrs_meas = models.FloatField(blank=True, null=True)
    unloct_flg = models.IntegerField(blank=True, null=True)
    crash_last_ud_dt = models.TextField(blank=True, null=True)
    tot_vhcl_cnt = models.IntegerField(blank=True, null=True)
    tot_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_inj_lvl_a_cnt = models.IntegerField(blank=True, null=True)
    tot_inj_lvl_b_cnt = models.IntegerField(blank=True, null=True)
    tot_inj_lvl_c_cnt = models.IntegerField(blank=True, null=True)
    tot_inj_cnt = models.IntegerField(blank=True, null=True)
    tot_uninjd_age00_04_cnt = models.IntegerField(blank=True, null=True)
    tot_uninjd_per_cnt = models.IntegerField(blank=True, null=True)
    tot_ped_cnt = models.IntegerField(blank=True, null=True)
    tot_ped_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_ped_inj_lvl_a_cnt = models.IntegerField(blank=True, null=True)
    tot_ped_inj_cnt = models.IntegerField(blank=True, null=True)
    tot_pedcycl_cnt = models.IntegerField(blank=True, null=True)
    tot_pedcycl_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_pedcycl_inj_lvl_a_cnt = models.IntegerField(blank=True, null=True)
    tot_pedcycl_inj_cnt = models.IntegerField(blank=True, null=True)
    tot_unknwn_cnt = models.IntegerField(blank=True, null=True)
    tot_unknwn_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_unknwn_inj_cnt = models.IntegerField(blank=True, null=True)
    tot_occup_cnt = models.IntegerField(blank=True, null=True)
    tot_per_invlv_cnt = models.IntegerField(blank=True, null=True)
    tot_sfty_equip_used_qty = models.IntegerField(blank=True, null=True)
    tot_sfty_equip_unused_qty = models.IntegerField(blank=True, null=True)
    tot_sfty_equip_use_unknown_qty = models.IntegerField(blank=True, null=True)
    tot_psngr_vhcl_occ_unrestrnd_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_mcyclst_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_mcyclst_inj_lvl_a_cnt = models.IntegerField(blank=True, null=True)
    tot_mcyclst_inj_cnt = models.IntegerField(blank=True, null=True)
    tot_mcyclst_unhelmtd_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_alchl_impaired_drvr_inv_fatal_cnt = models.IntegerField(blank=True, null=True)
    tot_drvr_age_01_20_cnt = models.IntegerField(blank=True, null=True)
    lane_rdwy_dprt_crash_flg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crash'


class CrashHr(models.Model):
    crash_hr_no = models.IntegerField(blank=True, null=True)
    crash_hr_long_desc = models.TextField(blank=True, null=True)
    crash_hr_med_desc = models.TextField(blank=True, null=True)
    crash_hr_short_desc = models.TextField(blank=True, null=True)
    crash_hr_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crash_hr'


class CrashKeyXref(models.Model):
    crash_key_xref_id = models.IntegerField(blank=True, null=True)
    crash_id = models.IntegerField(blank=True, null=True)
    vhcl_id = models.IntegerField(blank=True, null=True)
    partic_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crash_key_xref'


class CrashSvrty(models.Model):
    crash_svrty_cd = models.IntegerField(blank=True, null=True)
    crash_svrty_long_desc = models.TextField(blank=True, null=True)
    crash_svrty_short_desc = models.TextField(blank=True, null=True)
    crash_svrty_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crash_svrty'


class CrashTyp(models.Model):
    crash_typ_cd = models.TextField(blank=True, null=True)
    crash_typ_long_desc = models.TextField(blank=True, null=True)
    crash_typ_med_desc = models.TextField(blank=True, null=True)
    crash_typ_short_desc = models.TextField(blank=True, null=True)
    crash_typ_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crash_typ'


class DrvrLicStat(models.Model):
    drvr_lic_stat_cd = models.IntegerField(blank=True, null=True)
    drvr_lic_stat_long_desc = models.TextField(blank=True, null=True)
    drvr_lic_stat_short_desc = models.TextField(blank=True, null=True)
    drvr_lic_stat_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drvr_lic_stat'


class DrvrResStat(models.Model):
    drvr_res_stat_cd = models.IntegerField(blank=True, null=True)
    drvr_res_long_desc = models.TextField(blank=True, null=True)
    drvr_res_short_desc = models.TextField(blank=True, null=True)
    drvr_res_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drvr_res_stat'


class Err(models.Model):
    crash_err_cd = models.IntegerField(blank=True, null=True)
    crash_err_long_desc = models.TextField(blank=True, null=True)
    crash_err_med_desc = models.TextField(blank=True, null=True)
    crash_err_short_desc = models.TextField(blank=True, null=True)
    crash_err_partic_valid_flg = models.IntegerField(blank=True, null=True)
    crash_err_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'err'


class Evnt(models.Model):
    evnt_cd = models.IntegerField(blank=True, null=True)
    evnt_long_desc = models.TextField(blank=True, null=True)
    evnt_med_desc = models.TextField(blank=True, null=True)
    evnt_short_desc = models.TextField(blank=True, null=True)
    evnt_crash_valid_flg = models.IntegerField(blank=True, null=True)
    evnt_partic_valid_flg = models.IntegerField(blank=True, null=True)
    evnt_vhcl_valid_flg = models.IntegerField(blank=True, null=True)
    evnt_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evnt'


class FuncClass(models.Model):
    fc_cd = models.IntegerField(blank=True, null=True)
    fc_desc = models.TextField(blank=True, null=True)
    fc_start_yr_no = models.IntegerField(blank=True, null=True)
    fc_termnt_yr_no = models.IntegerField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)
    fc_short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'func_class'


class HwyCompnt(models.Model):
    hwy_compnt_cd = models.IntegerField(blank=True, null=True)
    hwy_compnt_long_desc = models.TextField(blank=True, null=True)
    hwy_compnt_med_desc = models.TextField(blank=True, null=True)
    hwy_compnt_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)
    hwy_compnt_short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hwy_compnt'


class HwyHist(models.Model):
    hwy_no = models.IntegerField(blank=True, null=True)
    hwy_sfx_no = models.NullBooleanField()
    hwy_long_nm = models.TextField(blank=True, null=True)
    hwy_med_nm = models.TextField(blank=True, null=True)
    hwy_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)
    alt_hwy_no = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hwy_hist'


class ImpctLoc(models.Model):
    impct_loc_cd = models.IntegerField(blank=True, null=True)
    impct_loc_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impct_loc'


class InjSvrty(models.Model):
    inj_svrty_cd = models.IntegerField(blank=True, null=True)
    inj_svrty_long_desc = models.TextField(blank=True, null=True)
    inj_svrty_med_desc = models.TextField(blank=True, null=True)
    inj_svrty_short_desc = models.TextField(blank=True, null=True)
    inj_svrty_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inj_svrty'


class InvstgAgy(models.Model):
    invstg_agy_cd = models.IntegerField(blank=True, null=True)
    invstg_agy_long_desc = models.TextField(blank=True, null=True)
    invstg_agy_short_desc = models.TextField(blank=True, null=True)
    invstg_agy_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invstg_agy'


class IsectTyp(models.Model):
    isect_typ_cd = models.IntegerField(blank=True, null=True)
    isect_typ_short_desc = models.TextField(blank=True, null=True)
    isect_typ_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isect_typ'


class JrsdctGrp(models.Model):
    jrsdct_grp_cd = models.IntegerField(blank=True, null=True)
    jrsdct_grp_long_desc = models.TextField(blank=True, null=True)
    jrsdct_grp_med_desc = models.TextField(blank=True, null=True)
    jrsdct_grp_short_desc = models.TextField(blank=True, null=True)
    jrsdct_grp_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jrsdct_grp'


class LgtCond(models.Model):
    lgt_cond_cd = models.IntegerField(blank=True, null=True)
    lgt_cond_long_desc = models.TextField(blank=True, null=True)
    lgt_cond_med_desc = models.TextField(blank=True, null=True)
    lgt_cond_short_desc = models.TextField(blank=True, null=True)
    lgt_cond_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lgt_cond'


class MednTyp(models.Model):
    medn_typ_cd = models.IntegerField(blank=True, null=True)
    medn_typ_long_desc = models.TextField(blank=True, null=True)
    medn_typ_short_desc = models.TextField(blank=True, null=True)
    medn_typ_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medn_typ'


class MlgeTyp(models.Model):
    mlge_typ_cd = models.TextField(blank=True, null=True)
    mlge_typ_long_desc = models.TextField(blank=True, null=True)
    mlge_typ_med_desc = models.TextField(blank=True, null=True)
    mlge_typ_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)
    mlge_typ_short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mlge_typ'


class Mvmnt(models.Model):
    mvmnt_cd = models.IntegerField(blank=True, null=True)
    mvmnt_long_desc = models.TextField(blank=True, null=True)
    mvmnt_med_desc = models.TextField(blank=True, null=True)
    mvmnt_short_desc = models.TextField(blank=True, null=True)
    mvmnt_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mvmnt'


class NonMotrstLoc(models.Model):
    non_motrst_loc_cd = models.IntegerField(blank=True, null=True)
    non_motrst_loc_long_desc = models.TextField(blank=True, null=True)
    non_motrst_loc_med_desc = models.TextField(blank=True, null=True)
    non_motrst_loc_short_desc = models.TextField(blank=True, null=True)
    non_motrst_loc_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'non_motrst_loc'


class Partic(models.Model):
    crash_id = models.IntegerField(blank=True, null=True)
    vhcl_id = models.IntegerField(blank=True, null=True)
    partic_id = models.IntegerField(primary_key=True)
    partic_dsply_seq_no = models.IntegerField(blank=True, null=True)
    vhcl_coded_seq_no = models.IntegerField(blank=True, null=True)
    partic_vhcl_seq_no = models.IntegerField(blank=True, null=True)
    partic_typ_cd = models.IntegerField(blank=True, null=True)
    partic_typ_short_desc = models.TextField(blank=True, null=True)
    partic_hit_run_flg = models.IntegerField(blank=True, null=True)
    pub_empl_flg = models.IntegerField(blank=True, null=True)
    sex_cd = models.IntegerField(blank=True, null=True)
    age_val = models.IntegerField(blank=True, null=True)
    drvr_lic_stat_cd = models.IntegerField(blank=True, null=True)
    drvr_lic_stat_short_desc = models.TextField(blank=True, null=True)
    drvr_res_stat_cd = models.IntegerField(blank=True, null=True)
    drvr_res_short_desc = models.TextField(blank=True, null=True)
    inj_svrty_cd = models.IntegerField(blank=True, null=True)
    inj_svrty_short_desc = models.TextField(blank=True, null=True)
    sfty_equip_use_cd = models.IntegerField(blank=True, null=True)
    sfty_equip_use_short_desc = models.TextField(blank=True, null=True)
    airbag_deploy_ind = models.IntegerField(blank=True, null=True)
    mvmnt_cd = models.IntegerField(blank=True, null=True)
    mvmnt_short_desc = models.TextField(blank=True, null=True)
    cmpss_dir_from_cd = models.IntegerField(blank=True, null=True)
    partic_cmpss_dir_from_short_desc = models.TextField(blank=True, null=True)
    cmpss_dir_to_cd = models.IntegerField(blank=True, null=True)
    partic_cmpss_dir_to_short_desc = models.TextField(blank=True, null=True)
    non_motrst_loc_cd = models.IntegerField(blank=True, null=True)
    non_motrst_loc_short_desc = models.TextField(blank=True, null=True)
    actn_cd = models.IntegerField(blank=True, null=True)
    actn_short_desc = models.TextField(blank=True, null=True)
    partic_err_1_cd = models.IntegerField(blank=True, null=True)
    partic_err_1_short_desc = models.TextField(blank=True, null=True)
    partic_err_2_cd = models.IntegerField(blank=True, null=True)
    partic_err_2_short_desc = models.TextField(blank=True, null=True)
    partic_err_3_cd = models.IntegerField(blank=True, null=True)
    partic_err_3_short_desc = models.TextField(blank=True, null=True)
    partic_cause_1_cd = models.IntegerField(blank=True, null=True)
    partic_cause_1_short_desc = models.TextField(blank=True, null=True)
    partic_cause_2_cd = models.IntegerField(blank=True, null=True)
    partic_cause_2_short_desc = models.TextField(blank=True, null=True)
    partic_cause_3_cd = models.IntegerField(blank=True, null=True)
    partic_cause_3_short_desc = models.TextField(blank=True, null=True)
    partic_evnt_1_cd = models.IntegerField(blank=True, null=True)
    partic_evnt_1_short_desc = models.TextField(blank=True, null=True)
    partic_evnt_2_cd = models.IntegerField(blank=True, null=True)
    partic_evnt_2_short_desc = models.TextField(blank=True, null=True)
    partic_evnt_3_cd = models.IntegerField(blank=True, null=True)
    partic_evnt_3_short_desc = models.NullBooleanField()
    bac_val = models.IntegerField(blank=True, null=True)
    alchl_use_rpt_ind = models.IntegerField(blank=True, null=True)
    drug_use_rpt_ind = models.IntegerField(blank=True, null=True)
    strikg_partic_flg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partic'


class ParticTyp(models.Model):
    partic_typ_cd = models.IntegerField(blank=True, null=True)
    partic_typ_long_desc = models.TextField(blank=True, null=True)
    partic_typ_med_desc = models.TextField(blank=True, null=True)
    partic_typ_short_desc = models.TextField(blank=True, null=True)
    partic_typ_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partic_typ'


class PopRng(models.Model):
    pop_rng_cd = models.IntegerField(blank=True, null=True)
    pop_rng_med_desc = models.TextField(blank=True, null=True)
    pop_rng_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pop_rng'


class RdChar(models.Model):
    rd_char_cd = models.IntegerField(blank=True, null=True)
    rd_char_long_desc = models.TextField(blank=True, null=True)
    rd_char_med_desc = models.TextField(blank=True, null=True)
    rd_char_short_desc = models.TextField(blank=True, null=True)
    rd_char_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rd_char'


class RdCntl(models.Model):
    rd_cntl_cd = models.IntegerField(blank=True, null=True)
    rd_cntl_med_desc = models.TextField(blank=True, null=True)
    rd_cntl_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)
    rd_cntl_long_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rd_cntl'


class RdSurfCond(models.Model):
    rd_surf_cond_cd = models.IntegerField(blank=True, null=True)
    rd_surf_med_desc = models.TextField(blank=True, null=True)
    rd_surf_short_desc = models.TextField(blank=True, null=True)
    rd_surf_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rd_surf_cond'


class Rdwy(models.Model):
    rdwy_no = models.IntegerField(blank=True, null=True)
    rdwy_desc = models.TextField(blank=True, null=True)
    rdwy_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rdwy'


class Rte(models.Model):
    rte_typ_cd = models.TextField(blank=True, null=True)
    rte_id = models.TextField(blank=True, null=True)
    rte_nm = models.TextField(blank=True, null=True)
    rte_hier_no = models.IntegerField(blank=True, null=True)
    rte_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rte'


class Sex(models.Model):
    sex_cd = models.IntegerField(blank=True, null=True)
    sex_desc = models.TextField(blank=True, null=True)
    sex_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sex'


class SftyEquipUse(models.Model):
    sfty_equip_use_cd = models.IntegerField(blank=True, null=True)
    sfty_equip_use_long_desc = models.TextField(blank=True, null=True)
    sfty_equip_use_med_desc = models.TextField(blank=True, null=True)
    sfty_equip_use_short_desc = models.TextField(blank=True, null=True)
    sfty_equip_use_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sfty_equip_use'


class SpeclJrsdct(models.Model):
    specl_jrsdct_id = models.IntegerField(blank=True, null=True)
    jrsdct_grp_cd = models.IntegerField(blank=True, null=True)
    specl_jrsdct_long_desc = models.TextField(blank=True, null=True)
    specl_jrsdct_med_desc = models.TextField(blank=True, null=True)
    specl_jrsdct_short_desc = models.TextField(blank=True, null=True)
    specl_jrsdct_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specl_jrsdct'


class TrafCntlDevice(models.Model):
    traf_cntl_device_cd = models.IntegerField(blank=True, null=True)
    traf_cntl_device_long_desc = models.TextField(blank=True, null=True)
    traf_cntl_device_short_desc = models.TextField(blank=True, null=True)
    traf_cntl_device_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traf_cntl_device'


class UrbArea(models.Model):
    urb_area_cd = models.IntegerField(blank=True, null=True)
    urb_area_long_nm = models.TextField(blank=True, null=True)
    urb_area_short_nm = models.TextField(blank=True, null=True)
    urb_area_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'urb_area'


class UrbAreaFipsHist(models.Model):
    urb_area_cd = models.IntegerField(blank=True, null=True)
    urb_area_hist_start_yr_no = models.IntegerField(blank=True, null=True)
    urb_area_hist_termnt_yr_no = models.IntegerField(blank=True, null=True)
    fips_urb_area_id = models.IntegerField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'urb_area_fips_hist'


class Vhcl(models.Model):
    crash_id = models.IntegerField(blank=True, null=True)
    vhcl_id = models.IntegerField(primary_key=True)
    vhcl_coded_seq_no = models.IntegerField(blank=True, null=True)
    vhcl_ownshp_cd = models.IntegerField(blank=True, null=True)
    vhcl_ownshp_short_desc = models.TextField(blank=True, null=True)
    vhcl_use_cd = models.IntegerField(blank=True, null=True)
    vhcl_use_short_desc = models.TextField(blank=True, null=True)
    vhcl_typ_cd = models.IntegerField(blank=True, null=True)
    vhcl_typ_short_desc = models.TextField(blank=True, null=True)
    emrgcy_vhcl_use_flg = models.IntegerField(blank=True, null=True)
    trlr_qty = models.IntegerField(blank=True, null=True)
    mvmnt_cd = models.IntegerField(blank=True, null=True)
    mvmnt_short_desc = models.TextField(blank=True, null=True)
    cmpss_dir_from_cd = models.IntegerField(blank=True, null=True)
    vhcl_cmpss_dir_from_short_desc = models.TextField(blank=True, null=True)
    cmpss_dir_to_cd = models.IntegerField(blank=True, null=True)
    vhcl_cmpss_dir_to_short_desc = models.TextField(blank=True, null=True)
    actn_cd = models.IntegerField(blank=True, null=True)
    actn_short_desc = models.TextField(blank=True, null=True)
    vhcl_cause_1_cd = models.IntegerField(blank=True, null=True)
    vhcl_cause_1_short_desc = models.TextField(blank=True, null=True)
    vhcl_cause_2_cd = models.IntegerField(blank=True, null=True)
    vhcl_cause_2_short_desc = models.TextField(blank=True, null=True)
    vhcl_cause_3_cd = models.IntegerField(blank=True, null=True)
    vhcl_cause_3_short_desc = models.TextField(blank=True, null=True)
    vhcl_evnt_1_cd = models.IntegerField(blank=True, null=True)
    vhcl_evnt_1_short_desc = models.TextField(blank=True, null=True)
    vhcl_evnt_2_cd = models.IntegerField(blank=True, null=True)
    vhcl_evnt_2_short_desc = models.TextField(blank=True, null=True)
    vhcl_evnt_3_cd = models.IntegerField(blank=True, null=True)
    vhcl_evnt_3_short_desc = models.TextField(blank=True, null=True)
    vhcl_speed_flg = models.IntegerField(blank=True, null=True)
    vhcl_hit_run_flg = models.IntegerField(blank=True, null=True)
    vhcl_sfty_equip_used_qty = models.IntegerField(blank=True, null=True)
    vhcl_sfty_equip_unused_qty = models.IntegerField(blank=True, null=True)
    vhcl_sfty_equip_use_unknwn_qty = models.IntegerField(blank=True, null=True)
    vhcl_occup_cnt = models.IntegerField(blank=True, null=True)
    strikg_vhcl_flg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vhcl'


class VhclOwnshp(models.Model):
    vhcl_ownshp_cd = models.IntegerField(blank=True, null=True)
    vhcl_ownshp_long_desc = models.TextField(blank=True, null=True)
    vhcl_ownshp_short_desc = models.TextField(blank=True, null=True)
    vhcl_ownshp_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vhcl_ownshp'


class VhclTyp(models.Model):
    vhcl_typ_cd = models.IntegerField(blank=True, null=True)
    vhcl_typ_long_desc = models.TextField(blank=True, null=True)
    vhcl_typ_short_desc = models.TextField(blank=True, null=True)
    vhcl_typ_termnt_dt = models.TextField(blank=True, null=True)
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vhcl_typ'


class VhclUse(models.Model):
    vhcl_use_cd = models.IntegerField(blank=True, null=True)
    vhcl_use_long_desc = models.TextField(blank=True, null=True)
    vhcl_use_short_desc = models.TextField(blank=True, null=True)
    vhcl_use_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vhcl_use'


class Wkday(models.Model):
    wkday_cd = models.IntegerField(blank=True, null=True)
    wkday_short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkday'


class WthrCond(models.Model):
    wthr_cond_cd = models.IntegerField(blank=True, null=True)
    wthr_cond_long_desc = models.TextField(blank=True, null=True)
    wthr_cond_med_desc = models.TextField(blank=True, null=True)
    wthr_cond_short_desc = models.TextField(blank=True, null=True)
    wthr_cond_termnt_dt = models.NullBooleanField()
    last_ud_dt = models.TextField(blank=True, null=True)
    last_ud_user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wthr_cond'
