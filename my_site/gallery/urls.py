from django.urls import path

from . import views

urlpatterns = [
    path('gallery/', views.album_view),
    path('<int:id>/', views.open_album, name='details'),
]
