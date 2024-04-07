import json
from django.http import JsonResponse
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WordToGuess, Game
from faker import Faker


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def start_game(request):
    if request.method == "POST":
        difficulty = request.POST.get("difficulty")
        try:
            difficulty = int(difficulty)
        except ValueError:
            return redirect("motus:home")
        except TypeError:
            return redirect("motus:home")
        list_length = range(difficulty - 1)
        if difficulty is None or difficulty == "" or difficulty < 3 or difficulty > 9:
            return redirect("motus:home")
        word = generate_word(difficulty)
        context = {
            "word_length": difficulty,
            "word": word,
            "first_letter": word.word_text[0],
            "list_length": list_length,
        }
        try:
            create_new_game(request.user)
        except IntegrityError:
            Game.objects.get(user=request.user).delete()
            create_new_game(request.user)

        return render(request, "game.html", context)
    else:
        return redirect("motus:home")


@login_required
def handle_guess(request):
    if request.method == "POST":
        data_dict = decode_json_request_body(request.body)
        guess = data_dict["guess"]
        word_id = data_dict["word_id"]
        word = WordToGuess.objects.get(pk=word_id)
        word_upper_text = word.word_text.upper()
        word_in_list = list(word_upper_text)
        guess_in_list = list(guess.upper())

        letter_counts = count_letter_occurrences(word_in_list)
        letters_positions = get_letter_positions(word_in_list)

        color_list, win = generate_color_list(
            word_in_list, guess_in_list, letter_counts, letters_positions
        )
        run = True
        if not win:
            game = Game.objects.get(user=request.user)
            game.life_point -= 1
            game.save()
            if game.life_point <= 0:
                run = False
        if win:
            request.user.ranking += 1 * len(guess)
            request.user.save()

        response = {"data": {"color_list": color_list, "win": win, "run": run}}
        if not run:
            response["data"]["word"] = word_upper_text

        return JsonResponse(response)

    return JsonResponse({"error": "Invalid request method"}, status=400)


@login_required
def win(request, word):
    return render(request, "win.html", {"word": word})


@login_required
def lose(request, word):
    return render(request, "lose.html", {"word": word})


def generate_word(difficulty: int) -> WordToGuess:
    """Generates a random word of the specified difficulty and saves it as a WordToGuess object.

    Args:
        difficulty (int): The desired length of the word to generate.

    Returns:
        WordToGuess: A newly created and saved WordToGuess object containing the generated word.

    Raises:
        ValueError: If the provided difficulty is more than 9.
    """  # noqa: E501
    if difficulty > 9:
        raise ValueError("Difficulty must be an integer lower than or equal to 9")
    fake = Faker()
    word = ""
    while len(word) != int(difficulty):
        word = fake.word()
    word_to_guess = WordToGuess(word_text=word)
    word_to_guess.save()
    return word_to_guess


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


def count_letter_occurrences(my_list):
    """Counts the occurrences of each letter in a list.

    Args:
        my_list: A list of characters.

    Returns:
        A dictionary where keys are unique characters from the list and values are their corresponding counts.
    """  # noqa: E501

    letter_counts = {}
    for letter in my_list:
        if letter in letter_counts:
            letter_counts[letter] += 1  # Increment count if letter exists
        else:
            letter_counts[letter] = 1  # Initialize count to 1 for new letter

    return letter_counts


def get_letter_positions(word_list):
    """
    Creates a dictionary mapping letters to their index positions in a list.

    Args:
        word_list: A list of characters.

    Returns:
        A dictionary where keys are unique characters from the list and values are lists containing their corresponding index positions.
    """  # noqa: E501

    letter_positions = {letter: [] for letter in set(word_list)}

    for i, letter in enumerate(word_list):
        letter_positions[letter].append(i)

    return letter_positions


def generate_color_list(
    word_in_list: list,
    guess_in_list: list,
    letter_counts: dict,
    letters_positions: dict,
) -> tuple[list, bool]:
    """Generates a list of color codes based on the guess compared to the word and determines if the guess represents a win.

    Args:
        word_in_list (list): A list of characters representing the word to be guessed (uppercase).
        guess_in_list (list): A list of characters representing the user's guess (uppercase).
        letter_counts (dict): A dictionary mapping letters to their occurrence counts in the word.
        letters_positions (dict): A dictionary mapping letters to a list of their positions in the word.

    Returns:
        tuple[list, bool]: A tuple containing a list of color codes ("red", "yellow", or "blue") for each letter in the guess and a boolean indicating if the guess is a win (all letters correctly placed).
    """  # noqa: E501
    if word_in_list == guess_in_list:
        color_list = ["red"] * len(word_in_list)
        win = True
    else:
        win = False
        color_list = ["blue"] * len(word_in_list)
        for i, letter in enumerate(guess_in_list):
            if letter in word_in_list:
                if i in letters_positions[letter]:
                    color_list[i] = "red"
                    letter_counts[letter] -= 1
        for i, letter in enumerate(guess_in_list):
            if letter in word_in_list:
                if i in letters_positions[letter]:
                    pass
                else:
                    if letter_counts[letter] > 0:
                        color_list[i] = "yellow"
                        letter_counts[letter] -= 1
    return color_list, win


def create_new_game(user):
    new_game = Game(user=user)
    new_game.save()
