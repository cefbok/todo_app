from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import *

class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = 'view_detail.html'
    context_object_name = 'task'

class CreateTask(CreateView):
    model = Task
    template_name = 'new_task.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class EditTask(UpdateView):
    model = Task
    template_name = 'edit_task.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    



