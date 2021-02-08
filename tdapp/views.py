from django.shortcuts import render, redirect
from .forms import *


def index(request):

    tasks = Task.objects.all()

    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def create_task(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tdapp:home')
    form = TaskForm

    context = {'form': form}
    return render(request, 'tdapp/create_task.html', context)


def update_task(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tdapp:home')

    context = {'form': form}
    return render(request, 'tdapp/create_task.html', context)


def delete_task(request, pk):

    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tdapp:home')

    context = {'task': task}
    return render(request, 'tdapp/delete_task.html', context)
