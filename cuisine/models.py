from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class FoodCategory(models.Model):
#     title = models.CharField(max_length=100,
#     unique=True)
    
#     def __str__(self):
#         return self.title


class Cuisine(models.Model):
    title = models.CharField(max_length=200,
    unique=True)
    slug = models.SlugField(max_length=200,
    unique=True)
    # category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE,
    # related_name='food_category')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name="recipe_posts")
    description = models.TextField(blank=True)
    instructions = models.TextField()
    
    def __str__(self):
        return self.title

# class Ingredients(models.Model):
#     category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE,
#     related_name='recipe_category')
#     recipe = models.ForeignKey(Cuisine, on_delete=models.CASCADE,
#     related_name='ingredients')
#     name = models.CharField(max_length=100)
#     quantity = models.CharField(max_length=50)

#     def __str__(self):
#         return f'{self.quantity} of {self.name} for {self.recipe.title}'


# class Comment(models.Model):
#     cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE,
#     related_name='comments')
#     author = models.ForeignKey(User, on_delete=models.CASCADE,
#     related_name='commenter')
#     body = models.TextField()
#     approved = models.BooleanField(default=False)
#     created_on = models.DateTimeField(auto_now_add=True)


#     class Meta:
#         ordering = ["-created_on"]

    
#     def __str__(self):
#         return f'Comment {self.body}. by {self.author}'
