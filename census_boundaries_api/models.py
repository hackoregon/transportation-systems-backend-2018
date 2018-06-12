from django.db import models
from django.contrib.gis.db import models

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class Tl201741Tabblock10(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    statefp10 = models.CharField(max_length=255, blank=True, null=True)
    countyfp10 = models.CharField(max_length=255, blank=True, null=True)
    tractce10 = models.CharField(max_length=255, blank=True, null=True)
    blockce10 = models.CharField(max_length=255, blank=True, null=True)
    geoid10 = models.CharField(max_length=255, blank=True, null=True)
    name10 = models.CharField(max_length=255, blank=True, null=True)
    mtfcc10 = models.CharField(max_length=255, blank=True, null=True)
    ur10 = models.CharField(max_length=255, blank=True, null=True)
    uace10 = models.CharField(max_length=255, blank=True, null=True)
    uatype = models.CharField(max_length=255, blank=True, null=True)
    funcstat10 = models.CharField(max_length=255, blank=True, null=True)
    aland10 = models.BigIntegerField(blank=True, null=True)
    awater10 = models.BigIntegerField(blank=True, null=True)
    intptlat10 = models.CharField(max_length=255, blank=True, null=True)
    intptlon10 = models.CharField(max_length=255, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tl_2017_41_tabblock10'
        in_db = 'census_gis'


class Tl201753Tabblock10(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    statefp10 = models.CharField(max_length=255, blank=True, null=True)
    countyfp10 = models.CharField(max_length=255, blank=True, null=True)
    tractce10 = models.CharField(max_length=255, blank=True, null=True)
    blockce10 = models.CharField(max_length=255, blank=True, null=True)
    geoid10 = models.CharField(max_length=255, blank=True, null=True)
    name10 = models.CharField(max_length=255, blank=True, null=True)
    mtfcc10 = models.CharField(max_length=255, blank=True, null=True)
    ur10 = models.CharField(max_length=255, blank=True, null=True)
    uace10 = models.CharField(max_length=255, blank=True, null=True)
    uatype = models.CharField(max_length=255, blank=True, null=True)
    funcstat10 = models.CharField(max_length=255, blank=True, null=True)
    aland10 = models.BigIntegerField(blank=True, null=True)
    awater10 = models.BigIntegerField(blank=True, null=True)
    intptlat10 = models.CharField(max_length=255, blank=True, null=True)
    intptlon10 = models.CharField(max_length=255, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tl_2017_53_tabblock10'
        in_db = 'census_gis'
