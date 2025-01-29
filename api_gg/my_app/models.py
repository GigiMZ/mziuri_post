from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField()
    edited = models.BooleanField(default=False)
    write_date = models.DateTimeField()
    
