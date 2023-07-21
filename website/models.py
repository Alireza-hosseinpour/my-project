from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=32)
    subject = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('created_at',)
    def __str__(self): 
        return self.name
    
    

class Newsletter(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email