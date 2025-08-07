from rest_framework.test import APITestCase
from users.factories.user import UserFactory


class CustomAPITestCase(APITestCase):
    url: str

    def setUp(self):
        super().setUp()
        self.user_login = UserFactory(username='test_user')
        self.client.force_authenticate(user=self.user_login)

    def get_url(self, id):
        return f'{self.url}{id}/'
