from django.test import TestCase
from odot_crash_api.models import Crash, Participant
from rest_framework.test import APIClient, RequestsClient

class CrashTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class CrashListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/odot-crash-data/crashes/')
        assert response.status_code == 200


class ParticipantTest(TestCase):
    """ Test for Participant model """

    def setUp(self):
        pass

class ParticipantListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/odot-crash-data/participants/')
        assert response.status_code == 200

class VehicleTest(TestCase):
    """ Test for Vehicle model """

    def setUp(self):
        pass

class VehicleListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/odot-crash-data/vehicles/')
        assert response.status_code == 200
