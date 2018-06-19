from django.test import TestCase
from multco_permits_api.models import CurrentPermits, ArchivedPermits
from rest_framework.test import APIClient, RequestsClient

class CurrentPermitsTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class CurrentPermitsListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/multnomah-county-permits/current/')
        assert response.status_code == 200

class ArchivedPermitsListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/multnomah-county-permits/archived/')
        assert response.status_code == 200
