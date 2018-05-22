# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SafetyHotlineTickets(models.Model):
    item_id = models.IntegerField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    problem_location = models.TextField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom_4326 = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'safety_hotline_tickets'
