from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Count, Case, When, Value, CharField
from django.db.models.functions import ExtractYear
import operator

def getAnnualTotals(census):
    census = census.values("summary_begin_date").distinct().annotate(
        total_routes=Count('route_number', distinct=True),
        total_stops=Count('stop_seq', distinct=True),
        year=ExtractYear("summary_begin_date"),
        ).order_by("summary_begin_date")
    return census

def getCounts(stops):
    annuals = stops.values(year=ExtractYear("summary_begin_date")).annotate(
        num_of_yearly_census=Count('summary_begin_date', distinct=True)).order_by("year")
    weekly = stops.filter(service_key__icontains="W").values(year=ExtractYear("summary_begin_date")).annotate(
        weekday_sum_ons=Sum('ons')*5*52/Count('summary_begin_date', distinct=True),
        weekday_sum_offs=Sum('offs')*5*52/Count('summary_begin_date', distinct=True),
        weekday_total_stops=Count('ons')*5*52/Count('summary_begin_date', distinct=True),
        ).order_by("year")
    saturday = stops.filter(service_key__icontains="S").values(year=ExtractYear("summary_begin_date")).annotate(
        saturday_sum_ons=Sum('ons')*52/Count('summary_begin_date', distinct=True),
        saturday_sum_offs=Sum('offs')*52/Count('summary_begin_date', distinct=True),
        saturday_total_stops=Count('ons')*52/Count('summary_begin_date', distinct=True)).order_by("year")
    sunday = stops.filter(service_key__icontains="U").values(year=ExtractYear("summary_begin_date")).annotate(
        sunday_sum_ons=Sum('ons')*52/Count('summary_begin_date', distinct=True),
        sunday_sum_offs=Sum('offs')*52/Count('summary_begin_date', distinct=True),
        sunday_total_stops=Count('ons')*52/Count('summary_begin_date', distinct=True)).order_by("year")
    sorting_key = operator.itemgetter("year")
    for i, j in zip(sorted(weekly, key=sorting_key), sorted(saturday, key=sorting_key)):i.update(j)
    for i, j in zip(sorted(weekly, key=sorting_key), sorted(sunday, key=sorting_key)):i.update(j)
    for i, j in zip(sorted(weekly, key=sorting_key), sorted(annuals, key=sorting_key)):i.update(j)
    for week in weekly:
        week["sunday_census"] = True
        week["saturday_census"] = True
        if  "saturday_sum_ons" not in week:
            week["saturday_sum_ons"] = 0
            week["saturday_sum_offs"]  = 0
            week["saturday_total_stops"] = 0
            week["saturday_census"] = False
        if "sunday_sum_ons" not in week:
            week["sunday_sum_ons"] = 0
            week["sunday_sum_offs"]  = 0
            week["sunday_total_stops"] = 0
            week["sunday_census"] = False
        week["annual_sum_ons"] = week["weekday_sum_ons"] + week["saturday_sum_ons"] + week["sunday_sum_ons"]
        week["annual_sum_offs"] = week["weekday_sum_offs"] + week["saturday_sum_offs"] + week["sunday_sum_offs"]
        week["total_annual_stops"] = week["weekday_total_stops"] + week["saturday_total_stops"] + week["sunday_total_stops"]
    return weekly
