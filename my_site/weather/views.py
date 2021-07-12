from django.shortcuts import render

from .forms import CityForm
import os
import requests

def weather_app(request):
    """ Получение прогноза погоды с сайта openweathermap """
    api_key = os.environ["api_wheather"] # Ключ (находится в переменной окружения)
    city = "Москва" # Город по умолчанию

    if request.method == "POST": # Если пользователь делает запрос
        form = CityForm(request.POST)
        if form.is_valid():
        # Если данные не прошли проверку, то атрибут cleaned_data будет содержать только значения тех полей, что прошли проверку
            city = form.cleaned_data['City']
    else:
        form = CityForm() # Очистка поля для формы ввода 

    url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + api_key + "&lang=ru"
    res = requests.get(url.format(city)).json() # Делаем запрос погоды по указанному городу

    city_info = {}

    try:
        city_info = {
                'city': city,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"],
                }
    except KeyError: # Если город с таким названием не найден
        city_info = {'error': 'Город не найден', 'temp': 'C'}

    form = CityForm()
    context = {'info': city_info, 'form': form}
    return context


def weather(request):
    context = weather_app(request)
    return render(request, 'weather/weatherPage.html', context)
