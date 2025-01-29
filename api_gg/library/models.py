from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL,
                               related_name='books', null=True, blank=True)


class Author(models.Model):
    name = models.CharField(max_length=100)