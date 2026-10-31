from django.urls import path
from .views import product_detail, product_edit, product_add, product_delete

urlpatterns = [
    path('<int:id>', product_detail, name= 'product_detail'),
    path('edit/<int:id>', product_edit, name= 'product_edit'),
    path('add', product_add, name= 'product_add'),
    path('delete/<int:id>', product_delete, name= 'product_delete')
]