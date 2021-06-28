from django.urls import path

from . import views

urlpatterns = [
    path('gallery/', views.album_view),
    path('gallery/<str:title_album>/', views.open_album, name='details'),
]
