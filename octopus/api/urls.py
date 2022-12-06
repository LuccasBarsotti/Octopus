from django.urls import path
from .views import ProductsList, ProductsDetail, InventoryList, InventoryDetail

urlpatterns = [
    path('products/<int:pk>/', ProductsDetail.as_view()),
    path('products/', ProductsList.as_view()),
    path('inventory/<int:pk>/', InventoryDetail.as_view()),
    path('inventory/', InventoryList.as_view()),
]