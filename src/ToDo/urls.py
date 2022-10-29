from django.contrib import admin
from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete


app_name = "ToDo"

urlpatterns = [
    path('<int:user_id>', TaskList.as_view(), name='home'),
    path('create/<int:task_id>', TaskCreate.as_view(), name='create'),
    path('edit/<int:task_id>', TaskDelete.as_view(), name='edit'),
    path('delete/<int:task_id>', TaskDelete.as_view(), name='delete'),
]
