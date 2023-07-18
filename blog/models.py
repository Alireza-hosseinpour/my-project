from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name
    
    

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/',default='camping-kampcilik-nedir.jpg')
    title = models.CharField(max_length=64)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    counted_view = models.IntegerField(default=0)
    published_data = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
