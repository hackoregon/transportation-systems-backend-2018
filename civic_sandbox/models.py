from django.contrib.gis.db import models

class SafetyHotlineTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    date_created = models.DateField()
    description = models.TextField(blank=True, null=True)
    geom_4326 = models.PointField()

    class Meta:
        managed = False
        db_table = 'safety_hotline_tickets'
        in_db = 'safety_hotline_tickets'