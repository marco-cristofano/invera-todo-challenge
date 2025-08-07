from rest_framework import status
from utils.testing.api_test import CustomAPITestCase
from tasks.factories.task import TaskFactory


class APITaskREtrieveTests(CustomAPITestCase):
    url = '/api/v1/tasks/'

    def setUp(self):
        super().setUp()
        self.task = TaskFactory()

    def test_retrieve(self):
        url = self.get_url(self.task.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = response.data
        self.assertEqual(len(task), 7)
        self.assertIsNotNone(task['id'])
        self.assertEqual(task['title'], self.task.title)
        self.assertEqual(task['description'], self.task.description)
        self.assertFalse(task['completed'])
        self.assertIsNotNone(task['user'])
        self.assertIsNotNone(task['created_at'])
        self.assertIsNotNone(task['updated_at'])
