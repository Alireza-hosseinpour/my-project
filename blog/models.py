from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)
    
class Tag(models.Model):
    name = models.CharField(max_length=64)
    

class Post(models.Model):
    #author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=64)
    content = models.TextField()
    #category = models.ManyToOneRel(Category,on_delete=models.CASCADE)
    #tag = models.ManyToOneRel(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    counted_view = models.IntegerField(default=0)
    published_data = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
