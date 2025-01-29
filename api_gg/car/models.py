from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    wheels = models.PositiveIntegerField(default=4)
    engine_size = models.FloatField(default=2.0)
    headlights = models.CharField(max_length=100)
    type = models.CharField(max_length=100)