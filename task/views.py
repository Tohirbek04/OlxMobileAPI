from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from task.filters import ProductFilter
from task.models import Product, Category
from task.serializers import ProductListSerializers, ProductRetrieveSerializers, CategoryModelSerializers, \
    ProductPostPutPatchSerializers


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializers


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializers


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductFilter
    ordering_fields = ['price', 'created_at']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSerializers
        return ProductPostPutPatchSerializers


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductRetrieveSerializers
        return ProductPostPutPatchSerializers



