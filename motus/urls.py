from django.urls import path
from .views import home, start_game, handle_guess, win, lose

urlpatterns = [
    path("", home, name="home"),
    path("game", start_game, name="start_game"),
    path("handle-guess", handle_guess, name="handle_guess"),
    path("win/<str:word>/", win, name="win"),
    path("lose/<str:word>/", lose, name="lose"),
]
