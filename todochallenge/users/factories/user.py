import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.LazyAttribute(lambda o: f"{o.username}@mail.com")
    password = factory.PostGenerationMethodCall('set_password', 'password')
