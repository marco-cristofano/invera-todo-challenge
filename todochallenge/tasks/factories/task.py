import factory
from tasks.models import Task
from users.factories.user import UserFactory


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = 'Title Task'
    description = factory.Sequence(lambda n: f'Description Task {n}')
    completed = False
    user = factory.SubFactory(UserFactory)
