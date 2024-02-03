from django.db import models
from django.contrib.auth.models import User
# task and todo models
class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    def __str__(self):
        return self.title
    
class Todo(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    tasks = models.ManyToManyField(Task)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_todos')

    def __str__(self):
        return self.title
    
