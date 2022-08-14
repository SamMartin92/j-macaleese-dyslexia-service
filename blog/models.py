from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title =models.CharField(max_length= 200, unique=True)
    slug = models.SlugField(max_length = 200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = models.ImageField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    