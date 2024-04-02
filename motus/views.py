import json
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
        data_dict = decode_json_request_body(request.body)
        guess = data_dict["guess"]
        word_id = data_dict["word_id"]
        word = WordToGuess.objects.get(pk=word_id)
        print(word)
        print(guess)
        feedback_data = ["red", "yellow", "blue"]

        return JsonResponse({"feedback": feedback_data})

    return JsonResponse({"error": "Invalid request method"}, status=400)


def decode_json_request_body(body_request: bytes) -> dict:
    """Decodes a request body and returns it as a Python dictionary.

    Args:
        body_request (bytes): The raw request body as a byte string.

    Returns:
        dict: The parsed JSON data as a Python dictionary.

    Raises:
        ValueError: If the request body cannot be decoded as UTF-8.
        json.JSONDecodeError: If the decoded request body is not valid JSON.
    """

    data_string = body_request.decode("utf-8")
    return json.loads(data_string)
