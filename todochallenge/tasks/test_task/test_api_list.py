from datetime import timedelta
from rest_framework import status
from tasks.factories.task import TaskFactory
from utils.testing.api_test import CustomAPITestCase


class APITaskListTests(CustomAPITestCase):
    url = '/api/v1/tasks/'

    def setUp(self):
        super().setUp()
        self.task = TaskFactory(description='filter description')
        self.task_2 = TaskFactory(description='filter')
        TaskFactory()

    def test_three_tasks(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tasks = response.data
        self.assertEqual(len(tasks), 3)
        task = tasks[0]
        self.assertEqual(len(task), 7)
        self.assertIsNotNone(task['id'])
        self.assertEqual(task['title'], self.task.title)
        self.assertEqual(task['description'], self.task.description)
        self.assertFalse(task['completed'])
        self.assertIsNotNone(task['user'])
        self.assertIsNotNone(task['created_at'])
        self.assertIsNotNone(task['updated_at'])

    def test_exact_filter_description(self):
        response = self.client.get(
            self.url, {'description': self.task.description}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tasks = response.data
        self.assertEqual(len(tasks), 1)
        task = tasks[0]
        self.assertEqual(len(task), 7)
        self.assertIsNotNone(task['id'])
        self.assertEqual(task['title'], self.task.title)
        self.assertEqual(task['description'], self.task.description)
        self.assertFalse(task['completed'])
        self.assertIsNotNone(task['user'])
        self.assertIsNotNone(task['created_at'])
        self.assertIsNotNone(task['updated_at'])

    def test_partial_filter_description(self):
        response = self.client.get(
            self.url, {'description': 'filter'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tasks = response.data
        self.assertEqual(len(tasks), 2)
        self.assertIsNotNone(tasks[0]['id'], self.task.id)
        self.assertIsNotNone(tasks[1]['id'], self.task_2.id)

    def test_empty_filter_description(self):
        response = self.client.get(
            self.url, {'description': 'not filter'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tasks = response.data
        self.assertEqual(len(tasks), 0)

    def test_filter_created_at(self):
        response = self.client.get(
            self.url, {'created_at': self.task.created_at.strftime('%Y-%m-%d')}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tasks = response.data
        self.assertEqual(len(tasks), 3)

    def test_empty_filter_created_at(self):
        date = (self.task.created_at + timedelta(days=1)).strftime('%Y-%m-%d')
        response = self.client.get(self.url, {'created_at': date})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tasks = response.data
        self.assertEqual(len(tasks), 0)

    def test_filter_bad_format_crated_at(self):
        date = (self.task.created_at + timedelta(days=1)).strftime('%Y/%m/%d')
        response = self.client.get(self.url, {'created_at': date})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertContains(
            response, 'created_at', status_code=status.HTTP_400_BAD_REQUEST
        )

    def test_filter_description_and_created_at_one_task(self):
        response = self.client.get(
            self.url,
            {
               'description': self.task.description,
               'created_at': self.task.created_at.strftime('%Y-%m-%d')
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tasks = response.data
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['id'], self.task.id)

    def test_filter_description_and_created_at_two_tasks(self):
        response = self.client.get(
            self.url,
            {
               'description': 'filter',
               'created_at': self.task.created_at.strftime('%Y-%m-%d')
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tasks = response.data
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]['id'], self.task.id)
        self.assertEqual(tasks[1]['id'], self.task_2.id)

    def test_filter_description_and_created_at_zero_tasks(self):
        response = self.client.get(
            self.url,
            {
               'description': 'bad_filter',
               'created_at': self.task.created_at.strftime('%Y-%m-%d')
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tasks = response.data
        self.assertEqual(len(tasks), 0)
