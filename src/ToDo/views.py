from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Task, User


# from .forms import SignUpForm

# Create your views here.


@method_decorator(login_required, name="dispatch")
class TaskList(ListView):
    model = Task
    context_object_name = 'todos'


@method_decorator(login_required, name="dispatch")
class TaskCreate(CreateView):
    model = Task
    fields = ["task", "completed"]


@method_decorator(login_required, name="dispatch")
class TaskUpdate(UpdateView):
    model = Task
    template_name = "ToDo/task_edit.html"


@method_decorator(login_required, name="dispatch")
class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("ToDo:home")

# class SignUpView(CreateView):
#     model = User
#     form_class = 'SignUpForm'
#     success_url = reverse_lazy()
