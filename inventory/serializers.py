from rest_framework import serializers
from .models import Warehouse, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "quantity",
            "warehouse",
        ]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            "id",
            "name",
        ]


class WarehouseDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(
        many=True,
        read_only=True,
        source="product_set",
    )

    class Meta:
        model = Warehouse
        fields = [
            "id",
            "name",
            "products",
        ]


class ProductPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            "name": {"read_only": True},
            "warehouse": {"read_only": True},
        }
