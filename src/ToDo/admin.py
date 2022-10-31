from django.contrib import admin
from .models import Task

# Register your models here.


admin.site.register(Task)

# class TaskAdmin(admin.ModelAdmin):
#     fields = "__all_"
#     list_display = "__all__"
#     list_editable = ("completed", )


# admin.site.register(Task, TaskAdmin)