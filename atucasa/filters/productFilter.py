''' File for filter in model product '''

from atucasa.models import Product

import django_filters


class ProductFilter(django_filters.rest_framework.FilterSet):
    ''' filters of products '''

    class Meta:
        model = Product
        fields = {
            'store': ['exact']
        }
        ordering_fields = ('store')
