import requests
from django.shortcuts import render
from .forms import CityForm

def base(request):
    return render(request, 'home/about_me.html')

def chat(request):
    return render(request, 'home/chat.html')

def weather(request):
    api_key = "da15c26ab6d1141108dd9109703d50d7" # Ключ при регистрации на openweathermap
    city = "Москва" # Город по умолчанию

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['City']
    else:
        form = CityForm()

    url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + api_key + "&lang=ru"
    res = requests.get(url.format(city)).json()

    city_info = {}

    try:
        city_info = {
                'city': city,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"],
                }
    except KeyError: # Если название не найдено
        city_info = {'error': 'Город не найден', 'temp': 'C'}

    form = CityForm() # Очистка поля формы
    context = {'info': city_info, 'form': form}
    return render(request, 'weather/weather.html', context)
