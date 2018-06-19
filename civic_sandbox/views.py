
from rest_framework.decorators import api_view

from .models import SafetyHotlineTickets, Crash, RouteChange, BlockChange, Sensor

from .serializers import SafetyHotlineSerializer, CrashSerializer, BlockChangeSerializer, RouteChangeSerializer, SensorSerializer
from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
from .helpers import sandbox_view_factory 
from .meta import safety_hotline_meta, crash_meta, route_change_meta, block_change_meta, sensors_meta



safetyhotline = sandbox_view_factory(
  model_class=SafetyHotlineTickets,
  serializer_class=SafetyHotlineSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom_4326',
  attributes =safety_hotline_meta['attributes'],
  dates=safety_hotline_meta['dates'],
  )

crash = sandbox_view_factory(
  model_class=Crash,
  serializer_class=CrashSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom_point',
  attributes =crash_meta['attributes'],
  dates=crash_meta['dates'],
  )


routechange = sandbox_view_factory(
  model_class=RouteChange,
  serializer_class=RouteChangeSerializer,
  multi_geom_class=MultiLineString,
  geom_field='geom_linestring',
  attributes =route_change_meta['attributes'],
  dates=route_change_meta['dates'],
  )


blockchange = sandbox_view_factory(
  model_class=BlockChange,
  serializer_class=BlockChangeSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom_polygon_4326',
  attributes =block_change_meta['attributes'],
  dates=block_change_meta['dates'],
  )

sensors = sandbox_view_factory(
  model_class=Sensor,
  serializer_class=SensorSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom_4326',
  attributes =sensors_meta['attributes'],
  dates=sensors_meta['dates'],
  )