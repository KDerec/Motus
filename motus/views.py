from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import WordGenerator


@login_required
def home(request):
    word_generator = WordGenerator()
    new_word = word_generator.get_new_word(5)
    return render(request, "home.html", {"new_word": new_word})


def start_game(request):
    if request.method == "POST":
        difficulty = request.POST.get("difficulty")
        return render(request, "game.html", {"word_length": difficulty})
