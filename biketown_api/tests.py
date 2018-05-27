from django.test import TestCase
from biketown_api.models import BiketownTrips
from rest_framework.test import APIClient, RequestsClient

class BiketownTripsTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class BiketownTripsListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/biketown/BiketownTrips/')
        assert response.status_code == 200
