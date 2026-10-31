from django.contrib import admin
from.models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    pass