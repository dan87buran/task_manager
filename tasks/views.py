from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from .tasks import send_task_notification


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        send_task_notification.delay(task.id, "created")
