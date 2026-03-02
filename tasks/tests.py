from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_task_creation(self):
        task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            user=self.user
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertFalse(task.completed)