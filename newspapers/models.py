from django.db import models
# Create your models here.
from django.urls import reverse

class Post(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField()
    date= models.DateField()
    author= models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    