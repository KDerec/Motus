import json
import pytest
from tests.conftest import MyData
from motus.models import WordToGuess
from motus.views import (
    decode_json_request_body,
    count_letter_occurrences,
    get_letter_positions,
    generate_word,
)


class StartGameTestCase(MyData):
    def setUp(self):
        """
        GIVEN: A logged-in user
        """
        self.client.force_login(self.user)

    def test_start_game_post_valid(self):
        """
        GIVEN: A user visits the start game page
        WHEN: The user selects a difficulty level (e.g., 4) and submits the form
        THEN: Access to game page
        """
        data = {"difficulty": "4"}
        response = self.client.post("/game", data=data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "game.html")
        self.assertEqual(response.context["word_length"], 4)

    def test_start_game_post_no_data(self):
        """
        GIVEN: A user visits the start game page
        WHEN: The user submits the form without selecting a difficulty
        THEN: Redirect to home page
        """
        data = {}
        response = self.client.post("/game", data=data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

    def test_start_game_post_empty_difficulty(self):
        """
        GIVEN: A user visits the start game page
        WHEN: The user submits the form with empty difficulty
        THEN: Redirect to home page
        """
        data = {"difficulty": ""}
        response = self.client.post("/game", data=data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

    def test_start_game_post_difficulty_below_minimum(self):
        """
        GIVEN: A user visits the start game page
        WHEN: The user submits the form with difficulty below 3
        THEN: Redirect to home page
        """
        data = {"difficulty": "2"}
        response = self.client.post("/game", data=data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

    def test_start_game_get(self):
        """
        GIVEN: A user visits the start game page
        WHEN: The user submits a GET request
        THEN: Redirect to home page
        """
        response = self.client.get("/game")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")


class DecodeJsonTestCase(MyData):
    def test_decode_json_request_body_valid_json(self):
        """Tests successful decoding of a valid JSON request body."""

        valid_json_data = b'{"key1": "value1", "key2": 42}'
        expected_result = {"key1": "value1", "key2": 42}

        result = decode_json_request_body(valid_json_data)

        assert result == expected_result

    def test_decode_json_request_body_invalid_json(self):
        """Tests handling of invalid JSON in the request body."""

        invalid_json_data = b'{"key1": "value1", key2": 42}'  # Missing a quote

        with pytest.raises(json.JSONDecodeError):
            decode_json_request_body(invalid_json_data)

    def test_decode_json_request_body_non_utf8_data(self):
        """Tests handling of non-UTF-8 data in the request body."""

        non_utf8_data = b"\x80abc"  # Non-UTF-8 byte sequence

        with pytest.raises(ValueError):
            decode_json_request_body(non_utf8_data)


class CountLetterOccurenceTestCase(MyData):
    def test_count_letter_occurrences_empty_list(self):
        """Tests handling of an empty list."""

        empty_list = []
        expected_result = {}

        result = count_letter_occurrences(empty_list)

        assert result == expected_result

    def test_count_letter_occurrences_single_letter(self):
        """Tests counting occurrences of a single letter."""

        single_letter_list = ["a"]
        expected_result = {"a": 1}

        result = count_letter_occurrences(single_letter_list)

        assert result == expected_result

    def test_count_letter_occurrences_multiple_letters(self):
        """Tests counting occurrences with multiple letters."""

        mixed_case_list = ["A", "A", "B"]
        expected_result = {"A": 2, "B": 1}

        result = count_letter_occurrences(mixed_case_list)

        assert result == expected_result


class GetLetterPositionTestCase(MyData):
    def test_get_letter_positions_empty_list(self):
        """Tests handling of an empty list."""

        empty_list = []
        expected_result = {}

        result = get_letter_positions(empty_list)

        assert result == expected_result

    def test_get_letter_positions_single_letter(self):
        """Tests positions for a single letter."""

        single_letter_list = ["a"]
        expected_result = {"a": [0]}

        result = get_letter_positions(single_letter_list)

        assert result == expected_result

    def test_get_letter_positions_repeated_letters(self):
        """Tests positions for letters appearing multiple times."""

        repeated_letters = ["a", "b", "a", "c"]
        expected_result = {"a": [0, 2], "b": [1], "c": [3]}

        result = get_letter_positions(repeated_letters)

        assert result == expected_result


class GenerateWordTestCase(MyData):
    def test_generate_word_valid_difficulty(self):
        """Tests successful word generation with valid difficulty."""

        difficulty = 5
        generated_word = generate_word(difficulty)

        assert isinstance(generated_word, WordToGuess)
        assert len(generated_word.word_text) == difficulty

    def test_generate_word_invalid_difficulty_too_high(self):
        """Tests handling of invalid difficulty (too high)."""

        difficulty = 10

        with pytest.raises(ValueError) as excinfo:
            generate_word(difficulty)

        assert (
            str(excinfo.value)
            == "Difficulty must be an integer lower than or equal to 9"
        )

    def test_generate_word_word_is_saved(self):
        """Tests that the generated word is saved in the database."""

        difficulty = 3
        generate_word(difficulty)

        saved_words = WordToGuess.objects.all()
        assert len(saved_words) == 1
