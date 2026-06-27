from django.urls import path
from .views import PostListView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
]