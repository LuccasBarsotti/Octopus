from rest_framework import serializers

from warehouse.models import Products, Inventory


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['name', 'bar_code', 'qtt', 'img']


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ['product', 'employee', 'qtt', 'mov', 'date']