from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.TextField(max_length=250)
    slug = models.SlugField()
    preparation_time = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)]
    ) 
    preparation_time_unit = models.CharField(max_length=12)
    servings = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)]
    )    
    servings_unit = models.CharField(max_length=12)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y%m%d/',
        blank=True, default='',
        )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null = True, 
        )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        blank = True, default=None,
        )
    
    def __str__(self):
        return self.title
