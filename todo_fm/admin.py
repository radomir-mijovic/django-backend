from django.contrib import admin
from .models import *


class TodoAdmin(admin.ModelAdmin):
    list_display = ['name', 'completed']


admin.site.register(Todos, TodoAdmin)
