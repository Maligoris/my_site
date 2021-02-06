from django.urls import path

from . import views

urlpatterns = [
    path('', views.base),
    path('weather/', views.weather),
    path('chat/', views.chat),
]
