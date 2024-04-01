from django.urls import path
from .views import home, start_game

urlpatterns = [
    path("", home, name="home"),
    path("game", start_game, name="start_game"),
]
