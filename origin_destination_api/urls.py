from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from origin_destination_api import views

# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'residence-area-characteristics', views.ResidenceAreaCharacteristicsViewSet)
router.register(r'workplace-area-characteristics', views.WorkplaceAreaCharacteristicsViewSet)
router.register(r'origin-destination', views.OriginDestinationViewSet)
router.register(r'xwalk', views.XwalkViewSet)
router.register(r'definitions', views.DefinitionsListViewSet,  base_name="origin-destination")
# schema_view = get_swagger_view(title='Hack Oregon 2018 Transportation Systems APIs')

urlpatterns = [
    # url(r'^schema/', schema_view),
    url(r'^', include(router.urls)),
    # url(r'^api/', include(router.urls)),
]
