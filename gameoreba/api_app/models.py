from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField()
    write_date = models.DateTimeField()
    publish_date = models.DateField()
    public = models.BooleanField(default=False)