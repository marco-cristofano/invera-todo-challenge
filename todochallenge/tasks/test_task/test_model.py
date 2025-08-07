from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.models import Task

User = get_user_model()


class TaskModelTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.completed_task = Task.objects.create(
            title='Title completed task',
            user=user,
            completed=True
        )
        self.incompleted_task = Task.objects.create(
            title='Title incompleted task',
            user=user,
            completed=False
        )

    def test_str_completed_task(self):
        self.assertEqual(
            str(self.completed_task),
            'Title completed task (testuser) Status: Completed'
        )

    def test_str_incompleted_task(self):
        self.assertEqual(
            str(self.incompleted_task),
            'Title incompleted task (testuser) Status: Not completed'
        )
