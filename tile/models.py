from django.db import models
from task.models import Tasks

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length = 15)

class Tiles(models.Model):
    tasks = models.ManyToManyField(Tasks, related_name='task_title')
    launch_date = models.CharField(max_length=20)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)