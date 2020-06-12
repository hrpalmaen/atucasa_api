''' File categories product views '''

from atucasa.models import Category_Product
from atucasa.serializer import CategoryProductSerializer

from rest_framework import viewsets


class CategoryProductView(viewsets.ModelViewSet):
    ''' categories product view '''
    # permission_code = 'category_product'
    queryset = Category_Product.objects.all()
    serializer_class = CategoryProductSerializer
