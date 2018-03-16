from django.db import models
from django.contrib.postgres.fields import JSONField

from django.template.defaultfilters import slugify

import pandas as pd

class CommandManager(models.Manager):
    pass

class Library(models.Model):
    library = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.library

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.library)
        super(Library, self).save(*arg, **kwargs)


class Command(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    section = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField()
    method = models.TextField()

    def __str__(self):
        return self.title

class DataFrame(models.Model):
    name = models.CharField(max_length=250)
    data = JSONField()
    preview = models.TextField()
    
    def __str__(self):
        return self.name

class Algorithm(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(max_length=250)

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.name)
        super(Algorithm, self).save(*arg, **kwargs)

    def __str__(self):
        return self.name

class PythonLibrary(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(max_length=250)

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.name)
        super(PythonLibrary, self).save(*arg, **kwargs)

    def __str__(self):
        return self.name
