from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from civic_sandbox import packages_view

urlpatterns = [
    url(r'^slides/safetyhotline/(?P<date_filter>\d+)', views.safetyhotline),
    url(r'^slides/safetyhotline/', views.safetyhotline),
    url(r'^slides/crashes/(?P<date_filter>\d+)', views.crash),
    url(r'^slides/crashes/', views.crash),
    url(r'^slides/routechange/', views.routechange),
    url(r'^foundations/blockchange/', views.blockchange),
    url(r'^slides/sensors/', views.sensors),
    url(r'^package_info/', packages_view.packages_view, name='package_info'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
