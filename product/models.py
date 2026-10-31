from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length= 300)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10,decimal_places=2, default= 0.00)
    image = models.ImageField(upload_to='product_image',default='default_product.png')
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, blank= True, null=True)
    
    
    class Meta:
        ordering = ['id','name']
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name