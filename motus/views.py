from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WordToGuess


@login_required
def home(request):
    return render(request, "home.html")


def start_game(request):
    if request.method == "POST":
        difficulty = request.POST.get("difficulty")
        if difficulty is None or difficulty == "" or int(difficulty) < 3:
            return redirect("motus:home")
        word = "test"
        word = WordToGuess(word_text=word)
        word.save()
        return render(request, "game.html", {"word_length": difficulty, "word": word})
    else:
        return redirect("motus:home")
