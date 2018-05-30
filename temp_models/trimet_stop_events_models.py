# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TrimetStopEvents(models.Model):
    service_date = models.DateField(blank=True, null=True)
    vehicle_number = models.IntegerField(blank=True, null=True)
    train = models.IntegerField(blank=True, null=True)
    route_number = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    trip_number = models.IntegerField(blank=True, null=True)
    service_key = models.TextField(blank=True, null=True)
    stop_time = models.IntegerField(blank=True, null=True)
    arrive_time = models.IntegerField(blank=True, null=True)
    seconds_late = models.IntegerField(blank=True, null=True)
    leave_time = models.IntegerField(blank=True, null=True)
    dwell = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    door = models.IntegerField(blank=True, null=True)
    lift = models.IntegerField(blank=True, null=True)
    ons = models.IntegerField(blank=True, null=True)
    offs = models.IntegerField(blank=True, null=True)
    estimated_load = models.IntegerField(blank=True, null=True)
    train_mileage = models.FloatField(blank=True, null=True)
    from_location = models.IntegerField(blank=True, null=True)
    mileage_there = models.FloatField(blank=True, null=True)
    left_there = models.IntegerField(blank=True, null=True)
    travel_miles = models.FloatField(blank=True, null=True)
    travel_seconds = models.IntegerField(blank=True, null=True)
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'trimet_stop_events'
