''' File products views '''

from atucasa.models import Product
from atucasa.serializer import ProductSerializer
from atucasa.filters import ProductFilter

from rest_framework import viewsets


class ProductView(viewsets.ModelViewSet):
    '''
    Vista Grupos - django
    '''
    # permission_code = 'product'
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter

    def get_queryset(self):
        params =  self.request.query_params
        star_param = params.get('star', False)
        if star_param:
            return Product.objects.all()[:10]
        return Product.objects.all()
