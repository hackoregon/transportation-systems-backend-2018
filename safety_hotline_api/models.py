from django.db import models
from django.contrib.gis.db import models

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

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
        in_db = 'safety_hotline_tickets'
