from django.urls import path

from . import views

urlpatterns = [
    path('games/', views.tictac_prelude),
    path('tictac/<room_code>', views.tictac),
]
