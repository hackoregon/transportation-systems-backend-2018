from django.test import TestCase
from census_boundaries_api.models import Tl201741Tabblock10, Tl201753Tabblock10
from rest_framework.test import APIClient, RequestsClient

class CensusTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class Tl201741Tabblock10ListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/census-boundaries/Tl201741Tabblock10/')
        assert response.status_code == 200

class Tl201753Tabblock10ListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/census-boundaries/Tl201753Tabblock10/')
        assert response.status_code == 200
