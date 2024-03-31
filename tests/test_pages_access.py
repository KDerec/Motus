from tests.conftest import MyData


class PageAccessTestCase(MyData):
    def setUp(self):
        """
        GIVEN: A logged-in user
        """
        self.client.force_login(self.admin_user)

    def test_can_access_to_admin_page(self):
        """
        WHEN: The user accesses the admin page
        THEN: They are granted access and a 200 status code is returned
        """
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)

    def test_can_access_to_home_page(self):
        """
        WHEN: The user accesses the home page
        THEN: They are granted access and a 200 status code is returned
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_can_access_to_password_change_page(self):
        """
        WHEN: The user accesses the password change page
        THEN: They are granted access and a 200 status code is returned
        """
        response = self.client.get("/password-change/")
        self.assertEqual(response.status_code, 200)

    def test_can_access_to_password_change_done_page(self):
        """
        WHEN: The user accesses the password change done page
        THEN: They are granted access and a 200 status code is returned
        """
        response = self.client.get("/password_change/done/")
        self.assertEqual(response.status_code, 200)


class PageForbiddenTestCase(MyData):
    def test_cant_access_to_admin_page(self):
        """
        WHEN: The unlogged user accesses the admin page
        THEN: They are redirected to login page and a 302 status code is returned
        """
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 302)
        assert "/login/" in response.url

    def test_cant_access_to_home_page(self):
        """
        WHEN: The unlogged user accesses the home page
        THEN: They are redirected to login page and a 302 status code is returned
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        assert "/login/" in response.url

    def test_cant_access_to_password_change_page(self):
        """
        WHEN: The unlogged user accesses the password change page
        THEN: They are redirected to login page and a 302 status code is returned
        """
        response = self.client.get("/password-change/")
        self.assertEqual(response.status_code, 302)
        assert "/login/" in response.url

    def test_cant_access_to_password_change_done_page(self):
        """
        WHEN: The unlogged user accesses the password change done page
        THEN: They are redirected to login page and a 302 status code is returned
        """
        response = self.client.get("/password_change/done/")
        self.assertEqual(response.status_code, 302)
        assert "/login/" in response.url
