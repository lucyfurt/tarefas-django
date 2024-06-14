from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Priority(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='task_category')
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='task_priority')
    file = models.FileField(upload_to='task_file/', blank=True, null=True)
    photo = models.ImageField(upload_to='task_photo/', blank=True)
    def __str__(self):
        return self.title
    
    
class TaskInventory(models.Model):
    task_count = models.IntegerField()
    
    def __str__(self):
        return self.task_count

