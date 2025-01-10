from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.TextField(max_length=160)
    slug = models.SlugField()
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=2)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y%m%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null = True
        )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
        )
