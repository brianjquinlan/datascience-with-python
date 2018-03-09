from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from ..views import *
from ..models import Post

from taggit.models import Tag
from django_comments.models import Comment

class TestPostListView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        
        user = User.objects.create(username='user')
        self.post = Post.objects.create(title='Test Post', body='post body', author=user)
        self.post2 = Post.objects.create(title='Test Post 2', body='body', author=user)
        self.post.tags.add('new tag')

        # comment = Comment.objects.create(content_type_id=7, site_id=1, comment='test comment')
        # print(comment)

        tags = Tag.objects.all()
        counts = tags.annotate(count = Count('taggit_taggeditem_items'))
        self.tag_counts = counts.values().order_by('-count')[:3]

    def test_get(self):
        request = self.factory.get(reverse('blog:post_list'))
        response = PostListView.as_view()(request)
        
        posts = Post.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context_data['top_tags'], map(repr, self.tag_counts))
        self.assertQuerysetEqual(response.context_data['posts'], map(repr, posts))

    def test_get_tag_list(self):
        tag = Tag.objects.get(name='new tag')
        tag_slug = tag.slug
        
        request = self.factory.get(reverse('blog:list_by_tag', 
            kwargs = {'tag_slug':tag_slug}))
        response = PostListView.as_view()(request, tag_slug=tag_slug)

        # print(response.__dict__)
        post = Post.objects.filter(tags__in=[tag])

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.context_data['comments'], comment)
        self.assertQuerysetEqual(response.context_data['top_tags'], map(repr, self.tag_counts))
        self.assertQuerysetEqual(response.context_data['posts'], map(repr, post))


class TestPostDetailView(TestCase):
    pass

class TestSubscribe(TestCase):
    pass
