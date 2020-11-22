from djongo import models

# Create your models here.

class Routine(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=150)
    capturedBy = models.CharField(max_length=150)
    points = models.JSONField()
    objects = models.DjongoManager()