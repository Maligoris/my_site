from django.test import TestCase

from django.test import SimpleTestCase

class SimpleTest(SimpleTestCase):
    def test_weather_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
