from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cuisine(models.Model):
    title = models.CharField(max_length=200,
    unique=True)
    slug = models.SlugField(max_length=200,
    unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name="recipe_posts")
    description = models.TextField(blank=True)
    instructions = models.TextField()
    
    def __str__(self):
        return self.title
