import django_filters
from django.db import models
from django_filters import FilterSet, NumberFilter

from task.models import Product


class ProductFilter(FilterSet):
    dan = NumberFilter(field_name='price', lookup_expr='gte')
    gacha = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['valyuta', 'category', 'status']









