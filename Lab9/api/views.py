from itertools import product
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer

from .models import Product, Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


