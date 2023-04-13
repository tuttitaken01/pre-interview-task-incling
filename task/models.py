from django.db import models
from tile.models import Tiles

# Create your models here.
class Types(models.Model):
    type = models.CharField(max_length = 30)

class Tasks(models.Model):
    title = models.CharField(max_length = 50)
    order = models.IntegerField()
    description = models.CharField(max_length = 150)
    type = models.ForeignKey(Types, on_delete=models.DO_NOTHING)
    tile_id = models.ForeignKey(Tiles, on_delete=models.DO_NOTHING)
    img = models.CharField(max_length = 200)

