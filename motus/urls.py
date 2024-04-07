from django.urls import path
from .views import home, start_game, handle_guess, win, lose, scoreboard, SignUpView

urlpatterns = [
    path("", home, name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("game", start_game, name="start_game"),
    path("handle-guess", handle_guess, name="handle_guess"),
    path("win/<str:word>/", win, name="win"),
    path("lose/<str:word>/", lose, name="lose"),
    path("scoreboard", scoreboard, name="scoreboard"),
]
