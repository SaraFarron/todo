from django.shortcuts import render, redirect

from .models import *
from .forms import *
from .decorators import *

from django.contrib import messages

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def index(request):

    tasks = Task.objects.all()

    context = {'tasks': tasks}
    return render(request, 'index.html', context)


# @login_required(login_url='login')
def create_task(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tdapp:home')
    form = TaskForm

    context = {'form': form}
    return render(request, 'tdapp/create_task.html', context)


# @login_required(login_url='login')
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


# @login_required(login_url='login')
def delete_task(request, pk):

    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tdapp:home')

    context = {'task': task}
    return render(request, 'tdapp/delete_task.html', context)


@unauthenticated_user
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tdapp:home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'tdapp/login.html', context)


def register_page(request):

    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get('guest')
            user.groups.add(group)
            Guest.objects.create(
                user=user,
                name=username,
            )
            messages.success(request, f'Account {username} created successfully')
            return redirect('tdapp:login')
        else:
            pass

    context = {'form': form}
    return render(request, 'tdapp/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('tdapp:login')


def profile_page(request):
    pass
