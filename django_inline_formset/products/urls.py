from django.urls import path

from .views import (
    ProductList, ProductCreate, ProductUpdate,
    delete_image, delete_variant
)

app_name = 'products'  # 3rd

urlpatterns = [
    path('products/', ProductList.as_view(), name='list_products'),
    path('create/', ProductCreate.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='update_product'),
    path('delete-image/<int:pk>/', delete_image, name='delete_image'),
    path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),
]
