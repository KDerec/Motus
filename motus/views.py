from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WordToGuess
from faker import Faker


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def start_game(request):
    if request.method == "POST":
        difficulty = request.POST.get("difficulty")
        difficulty = int(difficulty)
        if difficulty is None or difficulty == "" or difficulty < 3 or difficulty > 9:
            return redirect("motus:home")
        fake = Faker()
        word = ""
        while len(word) != int(difficulty):
            word = fake.word()
        word = WordToGuess(word_text=word)
        word.save()
        return render(request, "game.html", {"word_length": difficulty, "word": word})
    else:
        return redirect("motus:home")


@login_required
def handle_guess(request):
    if request.method == "POST":
        request.POST.get("guess")
        feedback_data = ["red", "yellow", "blue"]

        return JsonResponse({"feedback": feedback_data})

    return JsonResponse({"error": "Invalid request method"}, status=400)
