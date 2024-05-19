from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200,
    unique=True)
    slug = models.SlugField(max_length=200,
    unique=True)
    description = models.TextField(blank=True)
    instructions = models.TextField()
    
    def __str__(self):
        return self.title