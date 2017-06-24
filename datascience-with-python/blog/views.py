from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView, ArchiveIndexView, MonthArchiveView

from .models import Post
from taggit.models import Tag

# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/list.html'
    
    def get_queryset(self):
        qs = super().get_queryset()

        tag_slug = self.kwargs.get('tag_slug', None)
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            return qs.filter(tags__in=[tag])

        else:
            return qs[:10]

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

class ArchiveIndexView(ArchiveIndexView):
    queryset = Post.objects.all()

    context_object_name = 'post_list'
    date_field = 'published'

    template_name = 'blog/archive.html'

class MonthlyArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = 'published'
    
    template_name = 'blog/monthly_archive.html'
