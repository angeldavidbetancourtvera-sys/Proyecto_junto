from django.urls import path
from .views import PostUpdateView

urlpatterns = [
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
]
