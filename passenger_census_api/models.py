from django.db import models
from django.contrib.gis.db import models
from .routes import routes
import json

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class AnnualCensusBlockRidership(models.Model):
    year = models.IntegerField(blank=True, null=True)
    census_block = models.CharField(max_length=255, blank=True, null=True)
    total_ons = models.BigIntegerField(blank=True, null=True)
    stops = models.BigIntegerField(blank=True, null=True)
    geom_polygon_4326 = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'annual_census_block_ridership'
        in_db = 'passenger_census'


class AnnualRouteRidership(models.Model):
    year = models.IntegerField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    service_key = models.TextField(blank=True, null=True)
    total_ons = models.BigIntegerField(blank=True, null=True)
    total_offs = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'annual_route_ridership'
        in_db = 'passenger_census'


class CensusBlockChange(models.Model):
    census_block = models.CharField(primary_key=True, max_length=255)
    total_ons_2009 = models.BigIntegerField(blank=True, null=True)
    total_ons_2017 = models.BigIntegerField(blank=True, null=True)
    ons_pct_change = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    stops_2009 = models.BigIntegerField(blank=True, null=True)
    stops_2017 = models.BigIntegerField(blank=True, null=True)
    stops_pct_change = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    geom_polygon_4326 = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'census_block_change'
        in_db = 'passenger_census'


class OrCensusBlockPolygons(models.Model):
    census_block = models.CharField(primary_key=True, max_length=255)
    geom_polygon_4326 = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'or_census_block_polygons'
        in_db = 'passenger_census'


class PassengerCensus(models.Model):
    summary_begin_date = models.DateField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    service_key = models.TextField(blank=True, null=True)
    stop_seq = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    public_location_description = models.TextField(blank=True, null=True)
    ons = models.IntegerField(blank=True, null=True)
    offs = models.IntegerField(blank=True, null=True)
    x_coord = models.FloatField(blank=True, null=True)
    y_coord = models.FloatField(blank=True, null=True)
    geom_4326 = models.GeometryField(blank=True, null=True)
    census_block = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger_census'
        in_db = 'passenger_census'


class WaCensusBlockPolygons(models.Model):
    census_block = models.CharField(primary_key=True, max_length=255)
    geom_polygon_4326 = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wa_census_block_polygons'
        in_db = 'passenger_census'
