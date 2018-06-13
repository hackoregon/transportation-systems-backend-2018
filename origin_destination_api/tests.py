from django.test import TestCase
from origin_destination_api.models import ResidenceAreaCharacteristics, WorkplaceAreaCharacteristics, Xwalk
from rest_framework.test import APIClient, RequestsClient

class OriginDestinationTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class OriginDestinationListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/origin-destination/origin-destination/')
        assert response.status_code == 200

class ResidenceAreaCharacteristicsListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/origin-destination/residence-area-characteristics/')
        assert response.status_code == 200

class WorkplaceAreaCharacteristicsListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/origin-destination/workplace-area-characteristics/')
        assert response.status_code == 200

class XWalkListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/origin-destination/xwalk/')
        assert response.status_code == 200
