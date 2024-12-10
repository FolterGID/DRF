from rest_framework import viewsets
from .models import Product, Category
from .serializers import (
    CategoryReadSerializer,
    CategoryWriteSerializer,
    ProductReadSerializer,
    ProductWriteSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update" "destroy"):
            return CategoryWriteSerializer

        return CategoryReadSerializer


class ProductViewSet(viewsets.ModelViewSet):
     queryset = Product.objects.all()

     def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update" "destroy"):
            return ProductWriteSerializer

        return ProductReadSerializer
