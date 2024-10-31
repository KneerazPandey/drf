from django.urls import path
from . views import (
    ProductDetailAPIView, ProductListCreateAPIView
)


urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    
    path('', ProductListCreateAPIView.as_view(), name='product-create-list'),
]
