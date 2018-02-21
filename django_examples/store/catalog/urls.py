from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.products, name='product'),
]