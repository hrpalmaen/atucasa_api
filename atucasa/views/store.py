''' File stores views '''

from atucasa.models import Store
from atucasa.serializer import StoreSerializer

from rest_framework import viewsets


class StoreView(viewsets.ModelViewSet):
    ''' stores view '''
    # permission_code = 'store'
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
