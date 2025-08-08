import logging
from django.contrib.auth.models import User
from tasks.models import Task
logger = logging.getLogger('tasks')


class TaskLogger:

    @staticmethod
    def task_created(task: Task, user: User):
        log = f'Task created (id: {task.id}). User: {user.id}.'
        logger.info(log)

    @staticmethod
    def task_completed(task: Task, user: User):
        log = f'Task completed (id: {task.id}). User: {user.id}.'
        logger.info(log)
