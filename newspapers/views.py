from django.shortcuts import render
from .models import Post
from django.views.generic import UpdateView

# Create your views here.
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'update.html'