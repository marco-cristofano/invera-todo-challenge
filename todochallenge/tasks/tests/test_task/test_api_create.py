from rest_framework import status
from unittest.mock import patch
from utils.testing.api_test import CustomAPITestCase
from users.factories.user import UserFactory


class APITaskCreateTests(CustomAPITestCase):
    url = '/api/v1/tasks/'
    body = {
        'title': 'Title Task',
        'description': 'Description Task',
        'completed': False
    }

    def test_create(self):
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = response.data
        self.assertEqual(len(task), 7)
        self.assertIsNotNone(task['id'])
        self.assertEqual(task['title'], self.body['title'])
        self.assertEqual(task['description'], self.body['description'])
        self.assertFalse(task['completed'])
        self.assertIsNotNone(task['user'])
        self.assertIsNotNone(task['created_at'])
        self.assertIsNotNone(task['updated_at'])

    def test_create_without_description(self):
        body = self.body.copy()
        body.pop('description')
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = response.data
        self.assertIsNotNone(task['id'])
        self.assertEqual(task['title'], body['title'])
        self.assertEqual(task['description'], '')
        self.assertEqual(task['completed'], False)
        self.assertIsNotNone(task['user'])
        self.assertIsNotNone(task['created_at'])
        self.assertIsNotNone(task['updated_at'])

    def test_create_without_completed(self):
        body = self.body.copy()
        body.pop('completed')
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = response.data
        self.assertIsNotNone(task['id'])
        self.assertEqual(task['title'], body['title'])
        self.assertEqual(task['description'], body['description'])
        self.assertFalse(task['completed'])
        self.assertIsNotNone(task['user'])
        self.assertIsNotNone(task['created_at'])
        self.assertIsNotNone(task['updated_at'])

    def test_create_completed_true(self):
        body = self.body.copy()
        body['completed'] = True
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = response.data
        self.assertIsNotNone(task['id'])
        self.assertEqual(task['title'], body['title'])
        self.assertEqual(task['description'], body['description'])
        self.assertTrue(task['completed'])
        self.assertIsNotNone(task['user'])
        self.assertIsNotNone(task['created_at'])
        self.assertIsNotNone(task['updated_at'])

    def test_error_create_without_title(self):
        body = self.body.copy()
        body.pop('title')
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertContains(
            response, 'title', status_code=status.HTTP_400_BAD_REQUEST
        )

    def test_create_not_override_user(self):
        body = self.body.copy()
        user = UserFactory(username='test_user2')
        body['user'] = user
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['user']['id'], self.user_login.id)

    def test_create_not_override_created_at(self):
        body = self.body.copy()
        body['created_at'] = '2025-08-07T19:02:51.901145Z'
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(response.data['created_at'] == body['created_at'])

    def test_create_not_override_update_at(self):
        body = self.body.copy()
        body['updated_at'] = '2025-08-07T19:02:51.901145Z'
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(response.data['updated_at'] == body['updated_at'])

    @patch('tasks.loggers.logger')
    def test_create_with_log(self, mock_logger):
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task = response.data
        expected = f'Task created (id: {task["id"]}). User: {self.user_login.id}.'
        mock_logger.info.assert_called_once_with(expected)
