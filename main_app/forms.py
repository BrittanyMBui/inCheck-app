from django import forms
from .models import ToDo

class ToDoForm (forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['name', 'date_created', 'title', 'due_date', 'body', 'completed']
