from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', task_list_view, name='task_list'),
    path('task/create/', task_create_view, name='task_create'),
    path('task/update/<int:id>/', task_update_view, name='task_update'),
    path('task/delete/<int:id>/', task_delete_view, name='task_delete'),
    path('todo/create/', todo_create_view, name='todo_create'),
    path('todo/list/', todo_list_view, name='todo_list'),
    path('todo/update/<int:id>/', todo_update_view, name='todo_update'),
    path('todo/delete/<int:id>/', todo_delete_view, name='todo_delete'),
]