from rest_framework import status
from utils.testing.api_test import CustomAPITestCase
from tasks.factories.task import TaskFactory
from tasks.repositories.task import TaskRepository


class APITaskDeleteTests(CustomAPITestCase):
    url = '/api/v1/tasks/'

    def setUp(self):
        super().setUp()
        self.task = TaskFactory()

    def test_delete(self):
        url = self.get_url(self.task.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TaskRepository.count(), 0)
