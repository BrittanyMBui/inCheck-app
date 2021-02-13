from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import ToDo
from .forms import ToDoForm

def home(request):
    return render(request, 'home.html')

@login_required
def incheck_index(request):
    todos = ToDo.objects.filter(user=request.user)
    return render(request, 'incheck_index.html', {'todos': todos})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('incheck_index')
        else:
            error_message = 'Invalid Sign-up, try again'
    form  = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def view_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }

    return render(request, 'todos/view_todo.html', context)

@login_required
def create_todo(request):
    if request.method == "POST":
        todo_form = ToDoForm(request.POST)
        if todo_form.is_valid():
            new_todo = todo_form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('incheck_index')

    todo_form = ToDoForm()
    context = {
        'todo_form': todo_form
    }
    return render(request, 'todos/create_todo.html', context)

@login_required
def delete_todo(request, todo_id):
    if request.method == "POST":
        todo = ToDo.objects.get(id=todo_id)
        todo.delete()
        return redirect('incheck_index')

@login_required
def edit_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)

    if request.method == "GET":
        todo_form = ToDoForm(instance=todo)
        context = {
            'form': todo_form
        }
        return render(request, 'todos/edit_todo.html', context)
    
    else:
        todo_form = ToDoForm(request.POST, instance=todo)
        if todo_form.is_valid():
            todo_form.save()
            return redirect('view_todo', todo_id=todo_id)