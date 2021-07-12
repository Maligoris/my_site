from django.test import TestCase

from weather.views import *

class WeatherApp(TestCase):

    def test_weather_page(self):
        """ Проверка запроса погоды """
        api_key ="da15c26ab6d1141108dd9109703d50d7"
        form = CityForm({"City": "Лондон"})
        form.is_valid()
        city = form.cleaned_data['City']
        url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + api_key + "&lang=ru"

        response = requests.get(url.format(city)).json()
        self.assertEqual(response['cod'], 200)
        self.assertEqual(response['name'], "Лондон")
