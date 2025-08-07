from rest_framework import serializers
from tasks.models import Task
from users.serializers.user import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    completed = serializers.BooleanField(default=False)

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'completed',
            'created_at',
            'updated_at',
            'user'
        )
