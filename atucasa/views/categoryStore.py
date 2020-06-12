''' File categories store views '''

from atucasa.models import Category_Store
from atucasa.serializer import CategoryStoreSerializer

from rest_framework import viewsets


class CategoryStoreView(viewsets.ModelViewSet):
    ''' categories store view '''
    # permission_code = 'category_store'
    queryset = Category_Store.objects.all()
    serializer_class = CategoryStoreSerializer
