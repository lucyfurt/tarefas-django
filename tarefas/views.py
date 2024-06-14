from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from mimetypes import guess_type
from .models import Task
from  tarefas.forms import TaskModelForm
from django.views import View
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

#CRUD
class TaskListView(ListView):
    model = Task
    template_name = 'tarefas.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        tasks = super().get_queryset().order_by('title')
        search = self.request.GET.get('search')
        if search:
            tasks = tasks.filter(title__icontains=search)
        return tasks
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateTaskView(CreateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'new_task.html'
    success_url = '/tasks/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = '/tasks/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'update_task.html'
    
    def get_success_url(self):
        return  reverse_lazy('task_detail', kwargs={'pk': self.object.pk})
    

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

# FIM CRUD   
     
class DownloadTaskFile(View):
    def get(self, request, task_id):
        # Recupere a tarefa do banco de dados
        task = get_object_or_404(Task, id=task_id)
        
        # Verifique se o arquivo da tarefa existe
        if not task.file:
            return HttpResponse("Arquivo não encontrado.", status=404)
        
        # Abra o arquivo e leia o conteúdo
        with task.file.open() as f:
            file_content = f.read()
        
        # Determine o tipo de conteúdo do arquivo
        content_type, _ = guess_type(task.file.name)
        if content_type is None:
            content_type = 'application/octet-stream'  # Tipo de conteúdo padrão
        
        # Crie uma resposta HTTP com o conteúdo do arquivo
        response = HttpResponse(file_content, content_type=content_type)
        
        # Adicione o cabeçalho Content-Disposition para indicar que é um anexo que pode ser baixado
        response['Content-Disposition'] = f'attachment; filename="{task.file.name}"'
        
        return response