from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

from django.views.generic import ListView, DetailView, ArchiveIndexView, MonthArchiveView
from django.utils.decorators import method_decorator

from .models import Post
from taggit.models import Tag
from django_comments.models import Comment

from .utils import subscribe_email

# caching 
from django.views.decorators.cache import cache_page
from django.core.cache import cache

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/list.html'
    title = 'Blog List'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if cache.get('recent_comments') is not None:
            context['comments'] = cache.get('recent_comments')
        else:
            recent_comments = Comment.objects.all().prefetch_related('content_object').order_by('-id')[:3]
            cache.set('recent_comments', recent_comments)
            context['comments'] = recent_comments

        return context

    def get_queryset(self):
        qs = super().get_queryset()

        tag_slug = self.kwargs.get('tag_slug', None)
        if tag_slug:
            self.title = 'Posts tagged with %s' % tag_slug
            
            tag = get_object_or_404(Tag, slug=tag_slug)
        
            if cache.get('tagged_posts') is not None:
                return cache.get('tagged_posts')
            else:
                cache.set('tagged_posts', qs.select_related('author').filter(tags__in=[tag]))
                return qs.select_related('author').filter(tags__in=[tag])

        else:
            if cache.get('blog_posts') is not None:
                return cache.get('blog_posts')
            else:
                cache.set('blog_posts', qs.select_related('author')[:5])
                return qs.select_related('author')[:5]

    @method_decorator(cache_page(60*15))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
        
        cache_key = 'blog_' + str(post.slug)
        if cache.get(cache_key) is not None:
            return cache.get(cache_key)
        else:
            cache.set(cache_key, post)
            return post
    
    @method_decorator(cache_page(60*15))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ArchiveIndexView(ArchiveIndexView):
    queryset = Post.objects.all().select_related('author')

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
        status = subscribe_email(email)
   
        data = {
            'status_code': status
        }

        return JsonResponse(data)

    return HttpResponse("/")


