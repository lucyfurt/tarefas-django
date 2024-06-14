from django.contrib import admin
from tarefas.models import Task
from tarefas.models import Category
from tarefas.models import Priority

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'completed', 'category', 'priority')
    search_fields = ('title', 'description',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Priority, PriorityAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)

