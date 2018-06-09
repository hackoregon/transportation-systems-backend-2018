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
        # print(response.data)
        # self.assertEqual(response.data['year'], 2002)
        # self.assertEqual(response.data['weekday_sum_ons'], 456820)
        # self.assertEqual(response.data['weekday_sum_offs'], 453960)
        # self.assertEqual(response.data['weekday_total_stops'], 26520)
        # self.assertEqual(response.data['annual_sum_ons'], 509574)
        # self.assertEqual(response.data['annual_sum_offs'], 508300)
        # self.assertEqual(response.data['total_annual_stops'], 78520)
        # self.assertEqual(response.data['num_of_yearly_census'], 2)
    def test_missing_route(self):
        response = self.client.get('/transportation-systems/passenger-census/passenger-census-routes-annual/?year=2002')
        assert response.status_code == 400
        self.assertEqual(response.data, 'Missing Route Number paramater')
    def test_nonexistent_route(self):
        response = self.client.get('/transportation-systems/passenger-census/passenger-census-routes-annual/?route=678&year=2002')
        assert response.status_code == 404
        self.assertEqual(response.data, 'Route Number not found')
    # def test_nonexistent_route(self):
    #     response = self.client.get('/transportation-systems/passenger-census/passenger-census-route-annual/?route=1&year=2990')
    #     assert response.status_code == 404
    #     self.assertEqual(response.data, 'No Data found for Route Number and Year')
