from django.test import TestCase
from passenger_census_api.models import PassengerCensus
from rest_framework.test import APIClient, RequestsClient

class PassengerCensusTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class PassengerListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/passenger-census/passenger-census/')
        assert response.status_code == 200

class PassengerCensusRoutesEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/passenger-census/passenger-census-routes/')
        assert response.status_code == 200
        self.assertEqual(response.data['count'], 130)

class PassengerCensusRetrieveViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/passenger-census/passenger-census/675/')
        assert response.status_code == 200

class PassengerCensusRoutesAnnualEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_total_stops_response(self):
        response = self.client.get('/transportation-systems/passenger-census/passenger-census-routes-annual/?route=1&year=2002')
        assert response.status_code == 200
    def test_missing_route(self):
        response = self.client.get('/transportation-systems/passenger-census/passenger-census-routes-annual/?year=2002')
        assert response.status_code == 400
        self.assertEqual(response.data, 'Missing Route Number paramater')
    def test_nonexistent_route(self):
        response = self.client.get('/transportation-systems/passenger-census/passenger-census-routes-annual/?route=678&year=2002')
        assert response.status_code == 404
        self.assertEqual(response.data, 'Route Number not found')

class PassengerCensusInfoEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_total_stops_response(self):
        response = self.client.get('/transportation-systems/passenger-census/passenger-census-info/')
        assert response.status_code == 200
