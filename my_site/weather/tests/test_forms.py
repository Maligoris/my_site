from django.test import TestCase

from weather.forms import CityForm

class TestWeatherForm(TestCase):

    def test_weather_request_ru(self):
        """ Проверка ввода города на Русском """
        form = CityForm({"City": "Лондон"})
        form.is_valid()
        city = form.cleaned_data['City']
        self.assertEqual(city, "Лондон")

    def test_weather_request_en(self):
        """ Проверка ввода города на Английском """
        form = CityForm({"City": "London"})
        form.is_valid()
        city = form.cleaned_data['City']
        self.assertEqual(city, "London")
