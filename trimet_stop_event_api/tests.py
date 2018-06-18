from django.test import TestCase
from trimet_stop_event_api.models import TrimetStopEvents, TotalOnsByHour, DisturbanceStops
from rest_framework.test import APIClient, RequestsClient

class TrimetStopEventsTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class TrimetStopEventsListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/trimet-stop-events/trimet-stop-events/')
        assert response.status_code == 200

# class TrimetStopEventsTotalsListEndpointsTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#     def test_list_200_response(self):
#         response = self.client.get('/transportation-systems/trimet-stop-events/totals/')
#         assert response.status_code == 200

class DisturbanceStopsListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation-systems/trimet-stop-events/disturbance-stops/')
        assert response.status_code == 200
