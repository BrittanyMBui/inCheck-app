from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import ToDo

def home(request):
    return render(request, 'home.html')

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

def view_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }

    return render(request, 'todos/view_todo.html', context)
