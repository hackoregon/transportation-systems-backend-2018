from django.test import TestCase
from safety_hotline_api.models import SafetyHotlineTickets
from rest_framework.test import APIClient, RequestsClient

class SafetyHotlineTicketsTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class SafetyHotlineListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/safety_hotline/SafetyHotlineTickets/')
        assert response.status_code == 200

class SafetyHotlineListDescriptionFilterEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/safety_hotline/SafetyHotlineTickets/?description=street')

        assert response.status_code == 200
        self.assertEqual(response.data['count'], 1718)
        self.assertEqual(response.data['results']['type'], 'FeatureCollection')
