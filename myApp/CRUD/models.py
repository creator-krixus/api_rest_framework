from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
