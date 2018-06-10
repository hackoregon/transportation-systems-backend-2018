from django.test import TestCase
from passenger_census_api.models import PassengerCensus
from rest_framework.test import APIClient, RequestsClient

class PassengerCensusTest(TestCase):
    """ Test for Passenger Census model """

    def setUp(self):
        pass

class PassengerListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/passenger-census/')
        assert response.status_code == 200

class PassengerCensusRoutesEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/passenger-census/routes/')
        assert response.status_code == 200
        self.assertEqual(response.data['count'], 130)

class PassengerCensusRetrieveViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/passenger-census/675/')
        assert response.status_code == 200

class PassengerCensusRoutesAnnualEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_avg_total_stops_response(self):
        response = self.client.get('/transportation-systems/passenger-census/routes/annual/average/?route=1&year=2002')
        assert response.status_code == 200
    def test_avg_missing_route(self):
        response = self.client.get('/transportation-systems/passenger-census/routes/annual/average/?year=2002')
        assert response.status_code == 400
        self.assertEqual(response.data, 'Missing Route Number paramater')
    def test_avg_nonexistent_route(self):
        response = self.client.get('/transportation-systems/passenger-census/routes/annual/average/?route=678&year=2002')
        assert response.status_code == 404
        self.assertEqual(response.data, 'Route Number not found')
    def test_total_stops_response(self):
        response = self.client.get('/transportation-systems/passenger-census/routes/annual/total/?route=1&year=2002')
        assert response.status_code == 200
    def test_total_missing_route(self):
        response = self.client.get('/transportation-systems/passenger-census/routes/annual/total/?year=2002')
        assert response.status_code == 400
        self.assertEqual(response.data, 'Missing Route Number paramater')
    def test_total_nonexistent_route(self):
        response = self.client.get('/transportation-systems/passenger-census/routes/annual/total/?route=678&year=2002')
        assert response.status_code == 404
        self.assertEqual(response.data, 'Route Number not found')

class PassengerCensusInfoEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_total_stops_response(self):
        response = self.client.get('/transportation-systems/passenger-census/census/info/')
        assert response.status_code == 200
