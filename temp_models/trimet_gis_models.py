# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TmBoundary(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    area_sq_mi = models.FloatField(blank=True, null=True)
    acres = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_boundary'


class TmParkride(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    address = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    county = models.CharField(max_length=-1, blank=True, null=True)
    zipcode = models.CharField(max_length=-1, blank=True, null=True)
    owner = models.CharField(max_length=-1, blank=True, null=True)
    spaces = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_parkride'


class TmRailLines(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    line = models.CharField(max_length=-1, blank=True, null=True)
    passage = models.CharField(max_length=-1, blank=True, null=True)
    status = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_rail_lines'


class TmRailStops(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    station = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    line = models.CharField(max_length=-1, blank=True, null=True)
    status = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_rail_stops'


class TmRouteStops(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    rte = models.IntegerField(blank=True, null=True)
    dir = models.IntegerField(blank=True, null=True)
    rte_desc = models.CharField(max_length=-1, blank=True, null=True)
    dir_desc = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    stop_seq = models.IntegerField(blank=True, null=True)
    stop_id = models.IntegerField(blank=True, null=True)
    stop_name = models.CharField(max_length=-1, blank=True, null=True)
    jurisdic = models.CharField(max_length=-1, blank=True, null=True)
    zipcode = models.CharField(max_length=-1, blank=True, null=True)
    frequent = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_route_stops'


class TmRoutes(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    rte = models.IntegerField(blank=True, null=True)
    dir = models.IntegerField(blank=True, null=True)
    rte_desc = models.CharField(max_length=-1, blank=True, null=True)
    public_rte = models.CharField(max_length=-1, blank=True, null=True)
    dir_desc = models.CharField(max_length=-1, blank=True, null=True)
    frequent = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_routes'


class TmStops(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    stop_id = models.IntegerField(blank=True, null=True)
    stop_name = models.CharField(max_length=-1, blank=True, null=True)
    jurisdic = models.CharField(max_length=-1, blank=True, null=True)
    zipcode = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_stops'


class TmTranCen(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    address = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    county = models.CharField(max_length=-1, blank=True, null=True)
    zipcode = models.CharField(max_length=-1, blank=True, null=True)
    status = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_tran_cen'
