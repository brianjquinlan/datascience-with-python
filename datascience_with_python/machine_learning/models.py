from django.db import models
from django.contrib.postgres.fields import JSONField

import pandas as pd

class CommandManager(models.Manager):
    # def get_function(self):
    #    funct_name = self.library + self.title
    pass

class Command(models.Model):
    library = models.CharField(max_length=250)
    section = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField()
    method = models.TextField()

    def __str__(self):
        return self.title

class DataFrames(models.Model):
    name = models.CharField(max_length=250)
    data = JSONField()
    
    def __str__(self):
        return self.name

