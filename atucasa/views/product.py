''' File products views '''

from atucasa.models import Product
from atucasa.serializer import ProductSerializer

from rest_framework import viewsets


class ProductView(viewsets.ModelViewSet):
    '''
    Vista Grupos - django
    '''
    # permission_code = 'product'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
