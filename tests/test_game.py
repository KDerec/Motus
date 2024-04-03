from tests.conftest import MyData


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
