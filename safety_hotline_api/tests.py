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
        response = self.client.get('/transportation_systems_2018/safety_hotline/SafetyHotlineTickets/')
        assert response.status_code == 200
