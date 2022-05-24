from django.db import models
from django.utils import timezone
from django.contrib.postgres.indexes import GinIndex
 
 
class Batch(models.Model):
    create_date = models.DateTimeField(default=timezone.now)
    batch_id = models.CharField(max_length=64)

    def __str__(self):
        return self.batch_id


class Objects(models.Model):
    create_date = models.DateTimeField(default=timezone.now)
    object_id = models.CharField(max_length=64)
    data = models.JSONField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return self.object_id
        