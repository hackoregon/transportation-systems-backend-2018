from django.db import models

from django.contrib.gis.db import models


import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class DisturbanceStops(models.Model):
    serial = models.IntegerField(primary_key=True)
    opd_date_x = models.DateField(blank=True, null=True)
    vehicle_id_x = models.FloatField(blank=True, null=True)
    master_id_x = models.FloatField(blank=True, null=True)
    event_no_x = models.FloatField(blank=True, null=True)
    event_no_course = models.FloatField(blank=True, null=True)
    meters_x = models.FloatField(blank=True, null=True)
    act_dep_time_x = models.FloatField(blank=True, null=True)
    nom_dep_time_x = models.FloatField(blank=True, null=True)
    nom_end_time = models.FloatField(blank=True, null=True)
    act_end_time = models.FloatField(blank=True, null=True)
    line_id = models.FloatField(blank=True, null=True)
    course_id = models.FloatField(blank=True, null=True)
    trip_id = models.FloatField(blank=True, null=True)
    pattern_id = models.FloatField(blank=True, null=True)
    pattern_direction = models.TextField(blank=True, null=True)
    trip_type = models.FloatField(blank=True, null=True)
    highway_type = models.FloatField(blank=True, null=True)
    pattern_quality = models.FloatField(blank=True, null=True)
    block_id = models.FloatField(blank=True, null=True)
    passenger_data = models.FloatField(blank=True, null=True)
    time_grp_id = models.FloatField(blank=True, null=True)
    trip_code = models.FloatField(blank=True, null=True)
    driver_id = models.FloatField(blank=True, null=True)
    data_source = models.FloatField(blank=True, null=True)
    is_additional_trip = models.FloatField(blank=True, null=True)
    trip_role = models.TextField(blank=True, null=True)
    trip_subrole = models.TextField(blank=True, null=True)
    trip_purpose = models.FloatField(blank=True, null=True)
    event_no_y = models.FloatField(blank=True, null=True)
    event_no_trip = models.FloatField(blank=True, null=True)
    event_no_prev = models.FloatField(blank=True, null=True)
    opd_date_y = models.DateField(blank=True, null=True)
    vehicle_id_y = models.FloatField(blank=True, null=True)
    master_id_y = models.FloatField(blank=True, null=True)
    meters_y = models.FloatField(blank=True, null=True)
    act_arr_time = models.FloatField(blank=True, null=True)
    act_dep_time_y = models.FloatField(blank=True, null=True)
    nom_arr_time = models.FloatField(blank=True, null=True)
    nom_dep_time_y = models.FloatField(blank=True, null=True)
    point_id = models.FloatField(blank=True, null=True)
    stop_id = models.FloatField(blank=True, null=True)
    stop_pos = models.FloatField(blank=True, null=True)
    distance_to_next = models.FloatField(blank=True, null=True)
    distance_to_trip = models.FloatField(blank=True, null=True)
    doors_opening = models.FloatField(blank=True, null=True)
    positioning_method = models.FloatField(blank=True, null=True)
    stop_type = models.FloatField(blank=True, null=True)
    gps_longitude = models.FloatField(blank=True, null=True)
    gps_latitude = models.FloatField(blank=True, null=True)
    pattern_idx = models.FloatField(blank=True, null=True)
    door_open_time = models.FloatField(blank=True, null=True)
    point_role = models.TextField(blank=True, null=True)
    point_action = models.TextField(blank=True, null=True)
    plan_status = models.TextField(blank=True, null=True)
    time_diff = models.FloatField(blank=True, null=True)
    time_diff_min = models.FloatField(blank=True, null=True)
    geom_4326 = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disturbance_stops'
        in_db = 'trimet_stop_events'


class TotalsOnsByHour(models.Model):
    service_date = models.DateField(blank=True, null=True)
    service_key = models.TextField(blank=True, null=True)
    weekday = models.TextField(blank=True, null=True)
    hour_of_day = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_ons = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'totals_ons_by_hour'
        in_db = 'trimet_stop_events'


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
    x_coordinate = models.FloatField(blank=True, null=True)
    y_coordinate = models.FloatField(blank=True, null=True)
    geom_point_4326 = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trimet_stop_events'
        in_db = 'trimet_stop_events'
