from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

from django.views.generic import ListView, DetailView, ArchiveIndexView, MonthArchiveView

from .models import Post
from taggit.models import Tag

from .utils import subscribe_email

# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/list.html'
    title = 'Blog List'

    def get_queryset(self):
        qs = super().get_queryset()

        tag_slug = self.kwargs.get('tag_slug', None)
        if tag_slug:
            self.title = 'Posts tagged with %s' % tag_slug

            tag = get_object_or_404(Tag, slug=tag_slug)
            return qs.filter(tags__in=[tag])

        else:
            return qs[:10]
 
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_object(self):
        post = super().get_object()

        # view key for different blog posts
        key = 'viewed' + str(post)
 
        # increment view total
        if not self.request.session.get(key , False) and not self.request.user_agent.is_bot:   
            self.request.session[key] = True 
            
            post.views += 1
            post.save()
       
        return post

class ArchiveIndexView(ArchiveIndexView):
    queryset = Post.objects.all()

    context_object_name = 'post_list'
    date_field = 'published'

    template_name = 'blog/archive.html'

class MonthlyArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = 'published'
    
    template_name = 'blog/monthly_archive.html'

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email_id']
        subscribe_email(email)

    return HttpResponse("/")


