from unittest.mock import patch
from tasks.loggers import TaskLogger

from tasks.factories.task import TaskFactory
from utils.testing.api_test import APITestCase


class TestTaskLogger(APITestCase):

    def setUp(self):
        self.task = TaskFactory()
        self.user = self.task.user

    @patch('tasks.loggers.logger')
    def test_task_created_logs_info(self, mock_logger):
        TaskLogger.task_created(self.task, self.user)
        expected = f'Task created (id: {self.task.id}). User: {self.user.id}.'
        mock_logger.info.assert_called_once_with(expected)

    @patch('tasks.loggers.logger')
    def test_task_completed_logs_info(self, mock_logger):
        TaskLogger.task_completed(self.task, self.user)
        expected = f'Task completed (id: {self.task.id}). User: {self.user.id}.'
        mock_logger.info.assert_called_once_with(expected)
