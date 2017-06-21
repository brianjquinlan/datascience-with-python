from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=250)
    slug = models.SlugField()
    
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()

    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-published',)

    def get_absolute_url(self):
        pass

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
