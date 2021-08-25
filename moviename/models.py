from django.db import models
from django.db.models.fields import CharField

class MovieListModel(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    hero = models.CharField(max_length=50)
