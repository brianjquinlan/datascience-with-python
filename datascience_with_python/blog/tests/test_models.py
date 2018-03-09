from django.test import TestCase

from ..models import Post
from django.contrib.auth.models import User

class TestPost(TestCase):
    def setUp(self):
        user = User.objects.create(username='user')
        self.post = Post.objects.create(title='Test Post', author=user,
                body='post body')

    def test_str(self):
        post = Post.objects.get(title='Test Post')
        self.assertEqual(str(post), self.post.title)

    def test_slug(self):
        self.assertEqual('test-post', self.post.slug)
