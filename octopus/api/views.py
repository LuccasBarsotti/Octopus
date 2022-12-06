from rest_framework import generics

from warehouse.models import Products, Inventory
from .serializers import ProductsSerializer, InventorySerializer


class ProductsList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsDetail(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class InventoryList(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    
class InventoryDetail(generics.RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer