from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Post

class LatestPostsFeed(Feed):
    title = 'Machine Learning Blog'
    link = '/blog/'
    description = 'New posts of the blog'

    def items(self):
        return Post.objects.all()[:5]

    def items_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 20)
