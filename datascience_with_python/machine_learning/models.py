from django.db import models
from django.contrib.postgres.fields import JSONField

import pandas as pd

class CommandManager(models.Manager):
    pass

class Library(models.Model):
    library = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.library

class Command(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    section = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField()
    method = models.TextField()

    def __str__(self):
        return self.title

# do i need ?
class DataFrames(models.Model):
    name = models.CharField(max_length=250)
    data = JSONField()
    
    def __str__(self):
        return self.name

