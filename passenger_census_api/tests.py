from django.test import TestCase
from passenger_census_api.models import PassengerCensus
from rest_framework.test import APIClient, RequestsClient

class PassengerCensusTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class PassengerCensusListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation_systems_2018/passenger_census/PassengerCensus/')
        assert response.status_code == 200
