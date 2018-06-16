from django.contrib import admin
from .models import Task, Instance, History

# Register your models here.

admin.site.register(Task)
admin.site.register(Instance)
admin.site.register(History)