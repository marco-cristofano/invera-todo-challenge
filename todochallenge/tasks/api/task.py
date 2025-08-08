from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from tasks.models import Task
from tasks.repositories.task import TaskRepository
from tasks.serializers.task import TaskSerializer
from tasks.loggers import TaskLogger


class TaskFilter(filters.FilterSet):
    description = filters.CharFilter(lookup_expr='icontains')
    created_at = filters.DateFilter(lookup_expr='date')

    class Meta:
        model = Task
        fields = ['created_at', 'description']


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskRepository.all_with_user()
    serializer_class = TaskSerializer
    allowed_methods = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        TaskLogger.task_created(serializer.instance, user)

    def get_queryset(self):
        return TaskRepository.all_with_user()

    @action(detail=True, methods=['post'])
    def completed(self, request, pk=None):
        task = self.get_object()
        task.completed = True
        task.save()
        TaskLogger.task_completed(task, request.user)
        return Response(self.serializer_class(task).data)
