from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Count, Case, When, Value, CharField
from django.db.models.functions import ExtractYear
import operator, json
from .routes import routes
from .national import national
from .service_availability import availability

def getYearlyAvg(stops):
        annuals = stops.values(year=ExtractYear("summary_begin_date")).annotate(
            num_of_yearly_census=Count('summary_begin_date', distinct=True)).order_by("year")
        weekly = stops.filter(service_key__icontains="W").values(year=ExtractYear("summary_begin_date")).annotate(
            avg_weekday_sum_ons=(Sum('ons')*5*52/Count('summary_begin_date', distinct=True))/260,
            avg_weekday_sum_offs=(Sum('offs')*5*52/Count('summary_begin_date', distinct=True))/260,
            avg_weekday_stops=(Count('ons', distinct=True)*5*52/Count('summary_begin_date', distinct=True))/260
            ).order_by("year")
        saturday = stops.filter(service_key__icontains="S").values(year=ExtractYear("summary_begin_date")).annotate(
            avg_saturday_sum_ons=(Sum('ons')*52/Count('summary_begin_date', distinct=True))/52,
            avg_saturday_sum_offs=(Sum('offs')*52/Count('summary_begin_date', distinct=True))/52,
            avg_saturday_stops=(Count('ons', distinct=True)*52/Count('summary_begin_date', distinct=True))/260
            ).order_by("year")
        sunday = stops.filter(service_key__icontains="U").values(year=ExtractYear("summary_begin_date")).annotate(
            avg_sunday_sum_ons=(Sum('ons')*52/Count('summary_begin_date', distinct=True))/52,
            avg_sunday_sum_offs=(Sum('offs')*52/Count('summary_begin_date', distinct=True))/52,
            avg_sunday_stops=(Count('ons', distinct=True)*52/Count('summary_begin_date'))
            ).order_by("year")
        sorting_key = operator.itemgetter("year")
        for i, j in zip(sorted(weekly, key=sorting_key), sorted(saturday, key=sorting_key)):i.update(j)
        for i, j in zip(sorted(weekly, key=sorting_key), sorted(sunday, key=sorting_key)):i.update(j)
        for i, j in zip(sorted(weekly, key=sorting_key), sorted(annuals, key=sorting_key)):i.update(j)
        return weekly

# def getYearlyTotal(stops):
#         annuals = stops.values(year=ExtractYear("summary_begin_date")).annotate(
#             num_of_yearly_census=Count('summary_begin_date', distinct=True)).order_by("year")
#         weekly = stops.filter(service_key__icontains="W").values(year=ExtractYear("summary_begin_date")).annotate(
#             weekday_sum_ons=(Sum('ons')*5*52/Count('summary_begin_date', distinct=True)),
#             weekday_sum_offs=(Sum('offs')*5*52/Count('summary_begin_date', distinct=True)),
#             weekday_total_stops=(Count('ons', distinct=True)*5*52/Count('summary_begin_date', distinct=True))
#             ).order_by("year")
#         saturday = stops.filter(service_key__icontains="S").values(year=ExtractYear("summary_begin_date")).annotate(
#             saturday_sum_ons=(Sum('ons')*52/Count('summary_begin_date', distinct=True)),
#             saturday_sum_offs=(Sum('offs')*52/Count('summary_begin_date', distinct=True)),
#             saturday_total_stops=(Count('ons', distinct=True)*52/Count('summary_begin_date', distinct=True))
#             ).order_by("year")
#         sunday = stops.filter(service_key__icontains="U").values(year=ExtractYear("summary_begin_date")).annotate(
#             sunday_sum_ons=(Sum('ons')*52/Count('summary_begin_date', distinct=True)),
#             sunday_sum_offs=(Sum('offs')*52/Count('summary_begin_date', distinct=True)),
#             sunday_total_stops=(Count('ons', distinct=True)*52/Count('summary_begin_date', distinct=True))
#             ).order_by("year")
#         sorting_key = operator.itemgetter("year")
#         for i, j in zip(sorted(weekly, key=sorting_key), sorted(saturday, key=sorting_key)):i.update(j)
#         for i, j in zip(sorted(weekly, key=sorting_key), sorted(sunday, key=sorting_key)):i.update(j)
#         for i, j in zip(sorted(weekly, key=sorting_key), sorted(annuals, key=sorting_key)):i.update(j)
#         return weekly


def getYearlyTotal(stops):
        annuals = stops.values(year=ExtractYear("summary_begin_date")).annotate(
            num_of_yearly_census=Count('summary_begin_date', distinct=True)).order_by("year")
        weekly = stops.filter(service_key__icontains="W").values(year=ExtractYear("summary_begin_date")).annotate(
            weekday_sum_ons=Sum('ons')/Count('summary_begin_date', distinct=True),
            weekday_sum_offs=Sum('offs')/Count('summary_begin_date', distinct=True),
            weekday_total_stops=Count('ons', distinct=True)
            ).order_by("year")
        saturday = stops.filter(service_key__icontains="S").values(year=ExtractYear("summary_begin_date")).annotate(
            saturday_sum_ons=Sum('ons')/Count('summary_begin_date', distinct=True),
            saturday_sum_offs=Sum('offs')/Count('summary_begin_date', distinct=True),
            saturday_total_stops=Count('ons', distinct=True)
            ).order_by("year")
        sunday = stops.filter(service_key__icontains="U").values(year=ExtractYear("summary_begin_date")).annotate(
            sunday_sum_ons=Sum('ons')/Count('summary_begin_date', distinct=True),
            sunday_sum_offs=Sum('offs')/Count('summary_begin_date', distinct=True),
            sunday_total_stops=Count('ons', distinct=True)
            ).order_by("year")
        sorting_key = operator.itemgetter("year")
        for i, j in zip(sorted(weekly, key=sorting_key), sorted(saturday, key=sorting_key)):i.update(j)
        for i, j in zip(sorted(weekly, key=sorting_key), sorted(sunday, key=sorting_key)):i.update(j)
        for i, j in zip(sorted(weekly, key=sorting_key), sorted(annuals, key=sorting_key)):i.update(j)
        return weekly

def getAvgs(stops):
    weekly = getYearlyAvg(stops)
    for week in weekly:
        week["sunday_census"] = True
        week["saturday_census"] = True
        if  "avg_saturday_sum_ons" not in week:
            week["avg_saturday_sum_ons"] = 0
            week["avg_saturday_sum_offs"]  = 0
            week["avg_saturday_stops"] = 0
            week["saturday_census"] = False
        if "avg_sunday_sum_ons" not in week:
            week["avg_sunday_sum_ons"] = 0
            week["avg_sunday_sum_offs"]  = 0
            week["avg_sunday_stops"] = 0
            week["sunday_census"] = False
        week["avg_weekly_sum_ons"] = week["avg_weekday_sum_ons"] + week["avg_saturday_sum_ons"] + week["avg_sunday_sum_ons"]
        week["avg_weekly_sum_offs"] = week["avg_weekday_sum_offs"] + week["avg_saturday_sum_offs"] + week["avg_sunday_sum_offs"]
        week["avg_weekly_total_stops"] = week["avg_weekday_stops"] + week["avg_saturday_stops"] + week["avg_sunday_stops"]
    return weekly

def getTotals(stops):
    weekly = getYearlyTotal(stops)
    for week in weekly:
        week["sunday_census"] = True
        week["saturday_census"] = True
        if  "saturday_sum_ons" not in week:
            week["saturday_sum_ons"] = 0
            week["saturday_sum_offs"]  = 0
            week["saturday_total_stops"]  = 0
            week["saturday_census"] = False
        if "sunday_sum_ons" not in week:
            week["sunday_sum_ons"] = 0
            week["sunday_sum_offs"]  = 0
            week["sunday_total_stops"]  = 0
            week["sunday_census"] = False
        week["total_sum_ons"] = week["weekday_sum_ons"] + week["saturday_sum_ons"] + week["sunday_sum_ons"]
        week["total_sum_offs"] = week["weekday_sum_offs"] + week["saturday_sum_offs"] + week["sunday_sum_offs"]
        week["total_total_stops"] = week["weekday_total_stops"] + week["saturday_total_stops"] + week["sunday_total_stops"]

    return weekly

def getCensusTotals(census):
    weekly = census.filter(service_key__icontains="W").values("summary_begin_date").distinct().annotate(
        weekday_sum_ons=Sum('ons'),
        weekday_sum_offs=Sum('offs'),
        weekday_total_routes=Count('route_number', distinct=True),
        weekday_total_stops=Sum('ons')
        ).order_by("summary_begin_date")
    saturday = census.filter(service_key__icontains="S").values("summary_begin_date").distinct().annotate(
        saturday_sum_ons=Sum('ons'),
        saturday_sum_offs=Sum('offs'),
        saturday_total_routes=Count('route_number', distinct=True),
        saturday_total_stops=Sum('ons')
        ).order_by("summary_begin_date")
    sunday = census.filter(service_key__icontains="U").values("summary_begin_date").distinct().annotate(
        sunday_sum_ons=Sum('ons'),
        sunday_sum_offs=Sum('offs'),
        sunday_total_routes=Count('route_number', distinct=True),
        sunday_total_stops=Sum('ons')
        ).order_by("summary_begin_date")
    sorting_key = operator.itemgetter("summary_begin_date")
    for i, j in zip(sorted(weekly, key=sorting_key), sorted(saturday, key=sorting_key)):i.update(j)
    for i, j in zip(sorted(weekly, key=sorting_key), sorted(sunday, key=sorting_key)):i.update(j)
    for week in weekly:
        week["total_sum_ons"] = week["weekday_sum_ons"] + week["saturday_sum_ons"] + week["sunday_sum_ons"]
        week["total_sum_offs"] = week["weekday_sum_offs"] + week["saturday_sum_offs"] + week["sunday_sum_offs"]
        week["total_total_stops"] = week["weekday_total_stops"] + week["saturday_total_stops"] + week["sunday_total_stops"]

    return weekly

def routeDetailLookup(pk):
    dictdump = json.loads(routes)
    r = list(filter(lambda route: str(route['route_id']) == pk, dictdump))
    return r[0]

def nationalDetailLookup(pk):
    dictdump = json.loads(national)
    r = list(filter(lambda national: str(national['year']) == pk, dictdump))
    return r[0]
