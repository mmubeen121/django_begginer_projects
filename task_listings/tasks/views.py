from django.shortcuts import render, get_object_or_404
from .models import Task

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def task_detail(request, title):
    task = get_object_or_404(Task, title=title)
    return render(request, 'task_detail.html', {'task': task})
