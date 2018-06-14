from django.test import TestCase
from rest_framework.test import APIClient, RequestsClient

class CivicSandboxTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class CivicSandboxSafetyHotlineEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/sandbox/slides/safetyhotline/')
        assert response.status_code == 200

class CivicSandboxCrashesEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/sandbox/slides/crashes/')
        assert response.status_code == 200
