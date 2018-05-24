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

class PassengerCensusRoutesAnnualEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_total_stops_response(self):
        response = self.client.get('/transportation_systems_2018/passenger_census/PassengerCensusRoutesAnnual/?route=1&year=2002')
        assert response.status_code == 200
        self.assertEqual(response.data['total_stops'], 604)
        self.assertEqual(len(response.data['stops']['features']), 604)
        self.assertEqual(response.data['annual_sums']['sum_ons'], 144118)
        self.assertEqual(response.data['annual_sums']['sum_offs'], 145132)
    def test_missing_route(self):
        response = self.client.get('/transportation_systems_2018/passenger_census/PassengerCensusRoutesAnnual/?year=2002')
        assert response.status_code == 400
        self.assertEqual(response.data, 'Missing Route Number paramater')
    def test_missing_year(self):
        response = self.client.get('/transportation_systems_2018/passenger_census/PassengerCensusRoutesAnnual/?route=1')
        assert response.status_code == 400
        self.assertEqual(response.data, 'Must include a year for search')
    def test_nonexistent_route(self):
        response = self.client.get('/transportation_systems_2018/passenger_census/PassengerCensusRoutesAnnual/?route=678&year=2002')
        assert response.status_code == 404
        self.assertEqual(response.data, 'Route Number not found')
    def test_nonexistent_route(self):
        response = self.client.get('/transportation_systems_2018/passenger_census/PassengerCensusRoutesAnnual/?route=1&year=2990')
        assert response.status_code == 404
        self.assertEqual(response.data, 'No Data found for Route Number and Year')
