from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from census_boundaries_api import views

# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'Tl201741Tabblock10', views.Tl201741Tabblock10ViewSet)
router.register(r'Tl201753Tabblock10', views.Tl201753Tabblock10ViewSet)


# schema_view = get_swagger_view(title='Hack Oregon 2018 Transportation Systems APIs')

urlpatterns = [
    # url(r'^schema/', schema_view),
    url(r'^', include(router.urls)),
    # url(r'^api/', include(router.urls)),
]
