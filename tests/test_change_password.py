from tests.conftest import MyData


class ChangePasswordTestCase(MyData):
    def setUp(self):
        self.client.force_login(self.user)

    def test_user_can_change_password(self):
        """
        GIVEN: A logged-in user with a valid old password
        WHEN: They submit a password change form with valid new passwords
        THEN: The password is changed successfully and a success message is displayed
        """
        data = {
            "old_password": "motuslife13*",
            "new_password1": "Testpassword13$",
            "new_password2": "Testpassword13$",
        }
        response = self.client.post("/password-change/", data=data, follow=True)
        decoded_response = response.content.decode()
        self.assertEqual(200, response.status_code)
        assert "Votre mot de passe a été modifié." in decoded_response

    def test_password_change_wrong_old_password(self):
        """
        GIVEN: A logged-in user with an incorrect old password
        WHEN: They submit a password change form with valid new passwords
        THEN: An error message indicating the incorrect old password is displayed
        """
        data = {
            "old_password": "test",
            "new_password1": "Testpassword13$",
            "new_password2": "Testpassword13$",
        }
        response = self.client.post("/password-change/", data=data)
        decoded_response = response.content.decode()
        self.assertEqual(200, response.status_code)
        assert (
            "Votre ancien mot de passe est incorrect. Veuillez le rectifier."
            in decoded_response
        )

    def test_password_change_empty_old_password(self):
        """
        GIVEN: A logged-in user who submits a password change form with an empty old password field
        WHEN: They submit the form
        THEN: An error message indicating that the old password field is required is displayed
        """  # noqa: E501
        data = {
            "old_password": "",
            "new_password1": "Testpassword13$",
            "new_password2": "Testpassword13$",
        }
        response = self.client.post("/password-change/", data=data)
        decoded_response = response.content.decode()
        self.assertEqual(200, response.status_code)
        assert "Ce champ est obligatoire." in decoded_response

    def test_password_change_empty_password_one(self):
        """
        GIVEN: A logged-in user who submits a password change form with an empty new password 1 field
        WHEN: They submit the form
        THEN: An error message indicating that the new password 1 field is required is displayed
        """  # noqa: E501
        data = {
            "old_password": "test",
            "new_password1": "",
            "new_password2": "Testpassword13$",
        }
        response = self.client.post("/password-change/", data=data)
        decoded_response = response.content.decode()
        self.assertEqual(200, response.status_code)
        assert "Ce champ est obligatoire." in decoded_response

    def test_password_change_empty_password_two(self):
        """
        GIVEN: A logged-in user who submits a password change form with an empty new password 2 field
        WHEN: They submit the form
        THEN: An error message indicating that the new password 2 field is required is displayed
        """  # noqa: E501
        data = {
            "old_password": "test",
            "new_password1": "Testpassword13$",
            "new_password2": "",
        }
        response = self.client.post("/password-change/", data=data)
        decoded_response = response.content.decode()
        self.assertEqual(200, response.status_code)
        assert "Ce champ est obligatoire." in decoded_response

    def test_password_change_new_password_dont_match(self):
        """
        GIVEN: A logged-in user who submits a password change form with mismatched new passwords
        WHEN: They submit the form
        THEN: An error message indicating that the new passwords don't match is displayed
        """  # noqa: E501
        data = {
            "old_password": "motuslife13*",
            "new_password1": "Testpassword13$$",
            "new_password2": "Testpassword13",
        }
        response = self.client.post("/password-change/", data=data)
        decoded_response = response.content.decode()
        self.assertEqual(200, response.status_code)
        assert "Les deux mots de passe ne correspondent pas." in decoded_response

    def test_password_change_too_short(self):
        """
        GIVEN: A logged-in user who submits a password change form with a new password that is too short
        WHEN: They submit the form
        THEN: An error message indicating that the password is too short is displayed
        """  # noqa: E501
        data = {
            "old_password": "motuslife13*",
            "new_password1": "Test",
            "new_password2": "Test",
        }
        response = self.client.post("/password-change/", data=data)
        decoded_response = response.content.decode()
        self.assertEqual(200, response.status_code)
        assert (
            "Ce mot de passe est trop court. Il doit contenir au minimum 8 caractères."
            in decoded_response
        )
