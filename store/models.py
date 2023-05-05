from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    product_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    product_image = models.ImageField(upload_to="images/")
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)
    
    def __str__(self):
        return self.product_name
