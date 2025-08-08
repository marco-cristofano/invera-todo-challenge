from rest_framework import status
from utils.testing.api_test import APITestCase
from users.factories.user import UserFactory
from rest_framework.authtoken.models import Token


class APITaskListTests(APITestCase):
    url = '/logout/'

    def setUp(self):
        super().setUp()
        user = UserFactory(
            username='user',
            password='password'
        )
        self.token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_logout_success(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Token.objects.count(), 0)

    def test_logout_fail_token(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + f'{self.token.key}1'
        )
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
