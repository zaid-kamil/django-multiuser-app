from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.shortcuts import redirect
from .models import Task, Todo

# task views
@login_required(login_url='manager_login')
def task_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        assigned_to = request.POST.get('assigned_to')
        user = User.objects.get(username=assigned_to)
        task = Task(title=title, created_by=request.user, assigned_to=user)
        task.save()
        messages.success(request, 'Task created successfully')
        return redirect('task_list')
    employees = User.objects.filter(groups__name='employee')
    return render(request, 'todo/task_create.html',{
        'employees': employees
    })

def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html',{
        'tasks': tasks
    })

@login_required(login_url='manager_login')
def task_update_view(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.completed = request.POST.get('completed') == 'on'
        task.save()
        messages.success(request, 'Task updated successfully')
        return redirect('task_list')
    return render(request, 'todo/task_update.html',{
        'task': task
    })

@login_required(login_url='manager_login')
def task_delete_view(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('task_list')

# todo views
@login_required(login_url='employee_login')
def todo_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        tasks = request.POST.getlist('tasks') 
        todo = Todo(title=title, created_by=request.user)
        todo.save()
        for task_id in tasks:
            task = Task.objects.get(id=task_id)
            todo.tasks.add(task)
        messages.success(request, 'Todo created successfully')
        return redirect('todo_list')
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'todo/todo_create.html',{
        'tasks': tasks
    })

@login_required(login_url='employee_login')
def todo_list_view(request):
    todos = Todo.objects.filter(created_by=request.user)
    return render(request, 'todo/list.html',{
        'todos': todos
    })

@login_required(login_url='employee_login')
def todo_update_view(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.completed = request.POST.get('completed') == 'on'
        todo.save()
        messages.success(request, 'Todo updated successfully')
        return redirect('todo_list')
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'todo/todo_update.html',{
        'todo': todo,
        'tasks': tasks
    })

@login_required(login_url='employee_login')
def todo_delete_view(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    messages.success(request, 'Todo deleted successfully')
    return redirect('todo_list')