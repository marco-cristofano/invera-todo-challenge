from rest_framework import status
from utils.testing.api_test import CustomAPITestCase
from tasks.factories.task import TaskFactory


class APITaskCompletedTests(CustomAPITestCase):
    url = '/api/v1/tasks/'
    final_url = 'completed/'

    def setUp(self):
        super().setUp()
        self.task = TaskFactory(completed=False)

    def test_set_completed(self):
        url = self.get_url(self.task.id)
        response = self.client.post(url + self.final_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = response.data
        self.assertEqual(len(task), 7)
        self.assertIsNotNone(task['id'])
        self.assertEqual(task['title'], self.task.title)
        self.assertEqual(task['description'], self.task.description)
        self.assertTrue(task['completed'])
        self.assertIsNotNone(task['user'])
        self.assertIsNotNone(task['created_at'])
        self.assertIsNotNone(task['updated_at'])

    def test_set_completed_task_already_completed(self):
        self.task.completed = True
        self.task.save()
        url = self.get_url(self.task.id)
        response = self.client.post(url + self.final_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = response.data
        self.assertEqual(len(task), 7)
        self.assertIsNotNone(task['id'])
        self.assertEqual(task['title'], self.task.title)
        self.assertEqual(task['description'], self.task.description)
        self.assertTrue(task['completed'])
        self.assertIsNotNone(task['user'])
        self.assertIsNotNone(task['created_at'])
        self.assertIsNotNone(task['updated_at'])
