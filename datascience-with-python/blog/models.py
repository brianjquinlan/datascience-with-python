from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

from django.template.defaultfilters import slugify

# third party
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=250)
    slug = models.SlugField()
    
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog_posts/', blank=True, null=True)

    # published = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager()

    class Meta:
        ordering = ('-published',)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args= [self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
