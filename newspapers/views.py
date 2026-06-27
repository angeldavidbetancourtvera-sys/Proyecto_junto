from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, UpdateView, DetailView

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html' 

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'update.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'