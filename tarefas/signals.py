from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from tarefas.models import Task, TaskInventory

def task_inventory_update():
    task_count = Task.objects.all().count()
    TaskInventory.objects.create(
        task_count = task_count,     
    )

@receiver(post_save, sender=Task)
def task_post_save(sender, instance, **kwargs):
   task_inventory_update()

@receiver(post_delete, sender=Task)
def task_post_delete(sender, instance, **kwargs):
    task_inventory_update()
