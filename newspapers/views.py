from django.shortcuts import render
from .models import Post

from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'newspapers/post_list.html' 