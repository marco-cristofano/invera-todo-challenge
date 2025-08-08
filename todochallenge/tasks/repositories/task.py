from tasks.models import Task


class TaskRepository:

    @classmethod
    def all(cls):
        return Task.objects.all().order_by('created_at')

    @classmethod
    def count(cls):
        return Task.objects.count()

    @classmethod
    def all_with_user(cls):
        return cls.all().select_related('user')
