from django.shortcuts import render

from django.views.generic import ListView, DetailView, ArchiveIndexView, MonthArchiveView

from .models import Post

# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.all()[:10]

    context_object_name = 'posts'
    template_name = 'blog/list.html'

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
