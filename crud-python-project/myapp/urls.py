# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Frontend URLs
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/update/<int:product_id>/', views.product_update, name='product_update'),
    path('product/delete/<int:product_id>/', views.product_delete, name='product_delete'),

    # API URLs
    path('api/products/', views.api_product_list, name='api_product_list'),
    path('api/products/<int:product_id>/', views.api_product_detail, name='api_product_detail'),
    path('api/products/create/', views.api_product_create, name='api_product_create'),
    path('api/products/update/<int:product_id>/', views.api_product_update, name='api_product_update'),
    path('api/products/delete/<int:product_id>/', views.api_product_delete, name='api_product_delete'),
]
