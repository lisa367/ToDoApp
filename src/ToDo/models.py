from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

User = get_user_model()

class Task(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=700, verbose_name='Task')
    completed = models.BooleanField(default=False, verbose_name="Done")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Todo"
        ordering = ['completed', '-created_on']

    def get_absolute_url(self):
        return reverse('ToDo:index')