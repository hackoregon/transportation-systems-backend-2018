from django.db import models
from django.contrib.gis.db import models

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class BiketownTrips(models.Model):
    route_id = models.TextField(blank=True, null=True)
    payment_plan = models.TextField(blank=True, null=True)
    start_hub = models.TextField(blank=True, null=True)
    start_latitude = models.FloatField(blank=True, null=True)
    start_longitude = models.FloatField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_hub = models.TextField(blank=True, null=True)
    end_latitude = models.FloatField(blank=True, null=True)
    end_longitude = models.FloatField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    trip_type = models.TextField(blank=True, null=True)
    bike_id = models.TextField(blank=True, null=True)
    bike_name = models.TextField(blank=True, null=True)
    distance_miles = models.FloatField(blank=True, null=True)
    duration_text = models.TextField(blank=True, null=True)
    rental_access_path = models.TextField(blank=True, null=True)
    multiple_rental = models.TextField(blank=True, null=True)
    duration_minutes = models.FloatField(blank=True, null=True)
    start_geom_4326 = models.GeometryField(blank=True, null=True)
    end_geom_4326 = models.GeometryField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'biketown'
        in_db = 'biketown'
