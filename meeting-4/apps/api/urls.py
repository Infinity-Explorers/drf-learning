from django.urls import path

from .views import (ProductDetailAPIView,ProductListCreateAPIView)

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product'),
]