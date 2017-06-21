from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.all()

    context_object_name = 'posts'
    template_name = 'blog/list.html'

class PostDetailView(DetailView):
    model = Post

    template_name = 'blog/detail.html'
