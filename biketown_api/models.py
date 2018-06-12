from django.db import models
from django.contrib.gis.db import models

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class BiketownHubs(models.Model):
    hub = models.TextField(primary_key=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom_4326 = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biketown_hubs'
        in_db = 'biketown'

class BiketownTrips(models.Model):
    route_id = models.TextField(primary_key=True)
    payment_plan = models.TextField(blank=True, null=True)
    start_hub = models.ForeignKey(BiketownHubs, on_delete=models.CASCADE, db_column="start_hub", related_name="trips_start_hub")
    start_latitude = models.FloatField(blank=True, null=True)
    start_longitude = models.FloatField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_hub =  models.ForeignKey(BiketownHubs, on_delete=models.CASCADE, db_column="end_hub", related_name="trips_end_hub")
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

    @property
    def start_point(self):
        return self.start_hub.geom_4326

    @property
    def end_point(self):
        return self.end_hub.geom_4326

    class Meta:
        managed = False
        db_table = 'biketown'
        in_db = 'biketown'

class TripCounts(models.Model):
    start_hub = models.ForeignKey(BiketownHubs, on_delete=models.CASCADE, related_name="counts_start_hub")
    end_hub =  models.ForeignKey(BiketownHubs, on_delete=models.CASCADE, related_name="counts_end_hub")
    trips = models.BigIntegerField(blank=True, null=True)
    start_equals_end = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'trip_counts'
        unique_together = (('start_hub', 'end_hub'),)
        in_db = 'biketown'
