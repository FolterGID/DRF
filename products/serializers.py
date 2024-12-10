from rest_framework import serializers
from .models import Product, Category


class CategoryReadSerializer(serializers.ModelSerializer):
    """
    Serializer class for reading categories
    """

    class Meta:
        model = Category
        fields = "__all__"


class CategoryWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for reading categories
    """

    class Meta:
        model = Category
        fields = (
            "title",
            "created",
            "modified"
        )


class ProductReadSerializer(serializers.ModelSerializer):
    """
    Serializer class for reading products
    """

    seller = serializers.CharField(source="seller.get_username", read_only=True)
    category = serializers.CharField(source="category.title", read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "seller",
            "category",
            "title",
            "description",
            "image",
            "price",
            "stock",
            "created",
            "modified"
        )


class ProductWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for writing products
    """

    seller = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = (
            "seller",
            "category",
            "title",
            "description",
            "image",
            "price",
            "stock",
            "created",
            "modified"
        )

