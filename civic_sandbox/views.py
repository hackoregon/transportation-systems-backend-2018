
from rest_framework.decorators import api_view

from .models import SafetyHotlineTickets, Crash

from .serializers import SafetyHotlineSerializer, CrashSerializer
from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
from .helpers import sandbox_view_factory 
from .meta import safety_hotline_meta, crash_meta



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