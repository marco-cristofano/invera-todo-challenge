from django.test import TestCase
from django.contrib.auth import get_user_model
from users.factories.user import UserFactory
from tasks.factories.task import TaskFactory

User = get_user_model()


class TaskModelTest(TestCase):

    def setUp(self):
        user = UserFactory(username='testuser')
        self.completed_task = TaskFactory(user=user, completed=True)
        self.incompleted_task = TaskFactory(user=user, completed=False)

    def test_str_completed_task(self):
        self.assertEqual(
            str(self.completed_task),
            'Title Task (testuser) Status: Completed'
        )

    def test_str_incompleted_task(self):
        self.assertEqual(
            str(self.incompleted_task),
            'Title Task (testuser) Status: Not completed'
        )
