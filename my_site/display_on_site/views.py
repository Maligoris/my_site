from django.shortcuts import render

from weather.views import weather_app

def home(request):
    context = weather_app(request)
    return render(request, 'display_on_site/home.html', context)

def about_me(request):
    context = weather_app(request)
    return render(request, 'display_on_site/about_me.html', context)
