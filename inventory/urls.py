from django.urls import path
from .views import WarehouseListCreateView, ProductListCreateView, ProductUpdateView, WarehouseDetailView

urlpatterns = [
    path('warehouses/', WarehouseListCreateView.as_view(), name='warehouse-list-create'),
    path('warehouses/<int:pk>/', WarehouseDetailView.as_view(), name = 'warehouse-detail'),
    path('products/', ProductListCreateView.as_view(), name = 'product-list-create'),
    path('products/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
]