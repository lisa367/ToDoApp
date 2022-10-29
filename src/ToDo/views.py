from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task


class TaskCreate(CreateView):
    model = Task
    fields = ["task", "completed"]


class TaskUpdate(UpdateView):
    model = Task
    template_name = "ToDo/task_edit.html"


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("ToDo:home")