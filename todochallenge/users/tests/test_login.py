from rest_framework import status
from utils.testing.api_test import APITestCase
from users.factories.user import UserFactory


class APITaskListTests(APITestCase):
    url = '/login/'

    def setUp(self):
        super().setUp()
        UserFactory(
            username='user',
            password='password'
        )

    def test_login_success(self):
        body = {
            'username': 'user',
            'password': 'password'
        }
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data['token'])

    def test_login_fail(self):
        body = {
            'username': 'user',
            'password': 'bad_password'
        }
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertContains(
            response, 'credentials.', status_code=status.HTTP_400_BAD_REQUEST
        )
