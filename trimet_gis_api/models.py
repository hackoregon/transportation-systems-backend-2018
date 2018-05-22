from django.db import models
from django.contrib.gis.db import models

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class TmBoundary(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    area_sq_mi = models.FloatField(blank=True, null=True)
    acres = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_boundary'
        in_db = 'trimet_gis'

#
class TmParkride(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    spaces = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tm_parkride'
        in_db = 'trimet_gis'
#
#
# class TmRailLines(models.Model):
#     ogc_fid = models.AutoField(primary_key=True)
#     type = models.CharField(max_length=255, blank=True, null=True)
#     line = models.CharField(max_length=255, blank=True, null=True)
#     passage = models.CharField(max_length=255, blank=True, null=True)
#     status = models.CharField(max_length=255, blank=True, null=True)
#     wkb_geometry = models.GeometryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tm_rail_lines'
#         in_db = 'trimet_gis'
#
#
# class TmRailStops(models.Model):
#     ogc_fid = models.AutoField(primary_key=True)
#     station = models.CharField(max_length=255, blank=True, null=True)
#     type = models.CharField(max_length=255, blank=True, null=True)
#     line = models.CharField(max_length=255, blank=True, null=True)
#     status = models.CharField(max_length=255, blank=True, null=True)
#     wkb_geometry = models.GeometryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tm_rail_stops'
#         in_db = 'trimet_gis'
#
#
# class TmRouteStops(models.Model):
#     ogc_fid = models.AutoField(primary_key=True)
#     rte = models.IntegerField(blank=True, null=True)
#     dir = models.IntegerField(blank=True, null=True)
#     rte_desc = models.CharField(max_length=255, blank=True, null=True)
#     dir_desc = models.CharField(max_length=255, blank=True, null=True)
#     type = models.CharField(max_length=255, blank=True, null=True)
#     stop_seq = models.IntegerField(blank=True, null=True)
#     stop_id = models.IntegerField(blank=True, null=True)
#     stop_name = models.CharField(max_length=255, blank=True, null=True)
#     jurisdic = models.CharField(max_length=255, blank=True, null=True)
#     zipcode = models.CharField(max_length=255, blank=True, null=True)
#     frequent = models.CharField(max_length=255, blank=True, null=True)
#     wkb_geometry = models.GeometryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tm_route_stops'
#         in_db = 'trimet_gis'
#
#
# class TmRoutes(models.Model):
#     ogc_fid = models.AutoField(primary_key=True)
#     rte = models.IntegerField(blank=True, null=True)
#     dir = models.IntegerField(blank=True, null=True)
#     rte_desc = models.CharField(max_length=255, blank=True, null=True)
#     public_rte = models.CharField(max_length=255, blank=True, null=True)
#     dir_desc = models.CharField(max_length=255, blank=True, null=True)
#     frequent = models.CharField(max_length=255, blank=True, null=True)
#     type = models.CharField(max_length=255, blank=True, null=True)
#     wkb_geometry = models.GeometryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tm_routes'
#         in_db = 'trimet_gis'
#
#
# class TmStops(models.Model):
#     ogc_fid = models.AutoField(primary_key=True)
#     stop_id = models.IntegerField(blank=True, null=True)
#     stop_name = models.CharField(max_length=255, blank=True, null=True)
#     jurisdic = models.CharField(max_length=255, blank=True, null=True)
#     zipcode = models.CharField(max_length=255, blank=True, null=True)
#     type = models.CharField(max_length=255, blank=True, null=True)
#     wkb_geometry = models.GeometryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tm_stops'
#         in_db = 'trimet_gis'
#
#
# class TmTranCen(models.Model):
#     ogc_fid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     city = models.CharField(max_length=255, blank=True, null=True)
#     county = models.CharField(max_length=255, blank=True, null=True)
#     zipcode = models.CharField(max_length=255, blank=True, null=True)
#     status = models.CharField(max_length=255, blank=True, null=True)
#     wkb_geometry = models.GeometryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tm_tran_cen'
#         in_db = 'trimet_gis'
