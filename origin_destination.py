# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OriginDestination(models.Model):
    w_geocode = models.TextField(blank=True, null=True)
    h_geocode = models.TextField(blank=True, null=True)
    commuters = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'origin_destination'


class ResidenceAreaCharacteristics(models.Model):
    h_geocode = models.TextField(primary_key=True)
    c000 = models.IntegerField(blank=True, null=True)
    ca01 = models.IntegerField(blank=True, null=True)
    ca02 = models.IntegerField(blank=True, null=True)
    ca03 = models.IntegerField(blank=True, null=True)
    ce01 = models.IntegerField(blank=True, null=True)
    ce02 = models.IntegerField(blank=True, null=True)
    ce03 = models.IntegerField(blank=True, null=True)
    cns01 = models.IntegerField(blank=True, null=True)
    cns02 = models.IntegerField(blank=True, null=True)
    cns03 = models.IntegerField(blank=True, null=True)
    cns04 = models.IntegerField(blank=True, null=True)
    cns05 = models.IntegerField(blank=True, null=True)
    cns06 = models.IntegerField(blank=True, null=True)
    cns07 = models.IntegerField(blank=True, null=True)
    cns08 = models.IntegerField(blank=True, null=True)
    cns09 = models.IntegerField(blank=True, null=True)
    cns10 = models.IntegerField(blank=True, null=True)
    cns11 = models.IntegerField(blank=True, null=True)
    cns12 = models.IntegerField(blank=True, null=True)
    cns13 = models.IntegerField(blank=True, null=True)
    cns14 = models.IntegerField(blank=True, null=True)
    cns15 = models.IntegerField(blank=True, null=True)
    cns16 = models.IntegerField(blank=True, null=True)
    cns17 = models.IntegerField(blank=True, null=True)
    cns18 = models.IntegerField(blank=True, null=True)
    cns19 = models.IntegerField(blank=True, null=True)
    cns20 = models.IntegerField(blank=True, null=True)
    cr01 = models.IntegerField(blank=True, null=True)
    cr02 = models.IntegerField(blank=True, null=True)
    cr03 = models.IntegerField(blank=True, null=True)
    cr04 = models.IntegerField(blank=True, null=True)
    cr05 = models.IntegerField(blank=True, null=True)
    cr07 = models.IntegerField(blank=True, null=True)
    ct01 = models.IntegerField(blank=True, null=True)
    ct02 = models.IntegerField(blank=True, null=True)
    cd01 = models.IntegerField(blank=True, null=True)
    cd02 = models.IntegerField(blank=True, null=True)
    cd03 = models.IntegerField(blank=True, null=True)
    cd04 = models.IntegerField(blank=True, null=True)
    cs01 = models.IntegerField(blank=True, null=True)
    cs02 = models.IntegerField(blank=True, null=True)
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'residence_area_characteristics'
        unique_together = (('h_geocode', 'year'),)


class WorkplaceAreaCharacteristics(models.Model):
    w_geocode = models.TextField(primary_key=True)
    c000 = models.IntegerField(blank=True, null=True)
    ca01 = models.IntegerField(blank=True, null=True)
    ca02 = models.IntegerField(blank=True, null=True)
    ca03 = models.IntegerField(blank=True, null=True)
    ce01 = models.IntegerField(blank=True, null=True)
    ce02 = models.IntegerField(blank=True, null=True)
    ce03 = models.IntegerField(blank=True, null=True)
    cns01 = models.IntegerField(blank=True, null=True)
    cns02 = models.IntegerField(blank=True, null=True)
    cns03 = models.IntegerField(blank=True, null=True)
    cns04 = models.IntegerField(blank=True, null=True)
    cns05 = models.IntegerField(blank=True, null=True)
    cns06 = models.IntegerField(blank=True, null=True)
    cns07 = models.IntegerField(blank=True, null=True)
    cns08 = models.IntegerField(blank=True, null=True)
    cns09 = models.IntegerField(blank=True, null=True)
    cns10 = models.IntegerField(blank=True, null=True)
    cns11 = models.IntegerField(blank=True, null=True)
    cns12 = models.IntegerField(blank=True, null=True)
    cns13 = models.IntegerField(blank=True, null=True)
    cns14 = models.IntegerField(blank=True, null=True)
    cns15 = models.IntegerField(blank=True, null=True)
    cns16 = models.IntegerField(blank=True, null=True)
    cns17 = models.IntegerField(blank=True, null=True)
    cns18 = models.IntegerField(blank=True, null=True)
    cns19 = models.IntegerField(blank=True, null=True)
    cns20 = models.IntegerField(blank=True, null=True)
    cr01 = models.IntegerField(blank=True, null=True)
    cr02 = models.IntegerField(blank=True, null=True)
    cr03 = models.IntegerField(blank=True, null=True)
    cr04 = models.IntegerField(blank=True, null=True)
    cr05 = models.IntegerField(blank=True, null=True)
    cr07 = models.IntegerField(blank=True, null=True)
    ct01 = models.IntegerField(blank=True, null=True)
    ct02 = models.IntegerField(blank=True, null=True)
    cd01 = models.IntegerField(blank=True, null=True)
    cd02 = models.IntegerField(blank=True, null=True)
    cd03 = models.IntegerField(blank=True, null=True)
    cd04 = models.IntegerField(blank=True, null=True)
    cs01 = models.IntegerField(blank=True, null=True)
    cs02 = models.IntegerField(blank=True, null=True)
    cfa01 = models.IntegerField(blank=True, null=True)
    cfa02 = models.IntegerField(blank=True, null=True)
    cfa03 = models.IntegerField(blank=True, null=True)
    cfa04 = models.IntegerField(blank=True, null=True)
    cfa05 = models.IntegerField(blank=True, null=True)
    cfs01 = models.IntegerField(blank=True, null=True)
    cfs02 = models.IntegerField(blank=True, null=True)
    cfs03 = models.IntegerField(blank=True, null=True)
    cfs04 = models.IntegerField(blank=True, null=True)
    cfs05 = models.IntegerField(blank=True, null=True)
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'workplace_area_characteristics'
        unique_together = (('w_geocode', 'year'),)


class Xwalk(models.Model):
    tabblk2010 = models.TextField(primary_key=True)
    st = models.TextField(blank=True, null=True)
    stusps = models.TextField(blank=True, null=True)
    stname = models.TextField(blank=True, null=True)
    cty = models.TextField(blank=True, null=True)
    ctyname = models.TextField(blank=True, null=True)
    trct = models.TextField(blank=True, null=True)
    trctname = models.TextField(blank=True, null=True)
    bgrp = models.TextField(blank=True, null=True)
    bgrpname = models.TextField(blank=True, null=True)
    cbsa = models.TextField(blank=True, null=True)
    cbsaname = models.TextField(blank=True, null=True)
    zcta = models.TextField(blank=True, null=True)
    zctaname = models.TextField(blank=True, null=True)
    stplc = models.TextField(blank=True, null=True)
    stplcname = models.TextField(blank=True, null=True)
    ctycsub = models.TextField(blank=True, null=True)
    ctycsubname = models.TextField(blank=True, null=True)
    stcd115 = models.TextField(blank=True, null=True)
    stcd115name = models.TextField(blank=True, null=True)
    stsldl = models.TextField(blank=True, null=True)
    stsldlname = models.TextField(blank=True, null=True)
    stsldu = models.TextField(blank=True, null=True)
    stslduname = models.TextField(blank=True, null=True)
    stschool = models.TextField(blank=True, null=True)
    stschoolname = models.TextField(blank=True, null=True)
    stsecon = models.TextField(blank=True, null=True)
    stseconname = models.TextField(blank=True, null=True)
    trib = models.TextField(blank=True, null=True)
    tribname = models.TextField(blank=True, null=True)
    tsub = models.TextField(blank=True, null=True)
    tsubname = models.TextField(blank=True, null=True)
    stanrc = models.TextField(blank=True, null=True)
    stanrcname = models.TextField(blank=True, null=True)
    necta = models.TextField(blank=True, null=True)
    nectaname = models.TextField(blank=True, null=True)
    mil = models.TextField(blank=True, null=True)
    milname = models.TextField(blank=True, null=True)
    stwib = models.TextField(blank=True, null=True)
    stwibname = models.TextField(blank=True, null=True)
    blklatdd = models.FloatField(blank=True, null=True)
    blklondd = models.FloatField(blank=True, null=True)
    createdate = models.DateField(blank=True, null=True)
    geom_intpt_4326 = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xwalk'
