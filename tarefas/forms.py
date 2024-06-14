from django import forms
from tarefas.models import Task

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'



    
