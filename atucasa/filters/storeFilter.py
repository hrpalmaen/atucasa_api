''' File for filter in store with client '''

from atucasa.models import Store

import django_filters


class StoreFilter(django_filters.rest_framework.FilterSet):
    ''' filters of products '''

    class Meta:
        model = Store
        fields = {
            'id': ['exact'],
            'name': ['exact', 'contains'],
            'star': ['exact']
        }
        ordering_fields = ('id', 'name', 'star')
