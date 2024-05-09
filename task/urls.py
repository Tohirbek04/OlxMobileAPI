from django.urls import path

from .views import (CategoryRetrieveUpdateDestroyAPIView, CategoryListCreateAPIView,
                    ProductRetrieveUpdateDestroyAPIView, ProductListCreateAPIView)
urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>', CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('product/', ProductListCreateAPIView.as_view()),
    path('product/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view()),
]


