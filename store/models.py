from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

# class ProductCategory(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='categories')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

#     class Meta:
#         unique_together = ('product', 'category')

#     def __str__(self):
#         return f"{self.product.name} - {self.category.name}"