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
        response = self.client.get('/transportation-systems/passenger_census/PassengerCensus/')
        assert response.status_code == 200

class PassengerCensusRetrieveViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/passenger_census/PassengerCensus/675/')
        assert response.status_code == 200
        # self.assertEqual(response.data['geometry'], {
        #     "type": "Point",
        #     "coordinates": [
        #       -122.69685796828406,
        #       45.57720689855814
        #     ]
        #   })

class PassengerCensusRoutesAnnualEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_total_stops_response(self):
        response = self.client.get('/transportation-systems/passenger_census/PassengerCensusRoutesAnnual/?route=1&year=2002')
        assert response.status_code == 200
        self.assertEqual(response.data['total_stops'], 604)
        self.assertEqual(response.data['annual_sums']['sum_ons'], 144118)
        self.assertEqual(response.data['annual_sums']['sum_offs'], 145132)
        self.assertEqual(response.data['weekday_sums']['sum_ons'], 456820)
        self.assertEqual(response.data['weekday_sums']['sum_offs'], 453960)
        self.assertEqual(response.data['saturday_sums']['sum_ons'], 28574)
        self.assertEqual(response.data['saturday_sums']['sum_offs'], 30186)
        self.assertEqual(response.data['sunday_sums']['sum_ons'], 24180)
        self.assertEqual(response.data['sunday_sums']['sum_offs'], 24154)
    def test_missing_route(self):
        response = self.client.get('/transportation-systems/passenger_census/PassengerCensusRoutesAnnual/?year=2002')
        assert response.status_code == 400
        self.assertEqual(response.data, 'Missing Route Number paramater')
    def test_nonexistent_route(self):
        response = self.client.get('/transportation-systems/passenger_census/PassengerCensusRoutesAnnual/?route=678&year=2002')
        assert response.status_code == 404
        self.assertEqual(response.data, 'Route Number not found')
    def test_nonexistent_route(self):
        response = self.client.get('/transportation-systems/passenger_census/PassengerCensusRoutesAnnual/?route=1&year=2990')
        assert response.status_code == 404
        self.assertEqual(response.data, 'No Data found for Route Number and Year')
