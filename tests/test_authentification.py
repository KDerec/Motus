import pytest
from tests.conftest import MyData
from motus.models import User


class UserTestCase(MyData):
    def setUp(self):
        self.client.force_login(self.user)

    def test_users_exist_in_db(self):
        """
        GIVEN: Three users exist in the database (admin, user, user_two)
        WHEN: Their username are retrieved
        THEN: They match the expected values
        """
        self.assertEqual(self.admin_user.username, "admin")
        self.assertEqual(self.user.username, "user")
        self.assertEqual(self.user_two.username, "user_two")

    def test_create_user_with_empty_field(self):
        """
        GIVEN: New user creation with empty username and password
        WHEN: The create_user method is called
        THEN: A ValueError is raised
        """
        with pytest.raises(ValueError):
            User.objects.create_user(username="", password="", is_staff=True)

    def test_user_can_login(self):
        """
        GIVEN: A logged-in user (user)
        WHEN: The home page is accessed
        THEN: The user is authenticated in the response context
        """
        response = self.client.get("/")
        self.assertTrue(response.context["user"].is_authenticated)
