''' File stores views '''

from atucasa.models import Store
from atucasa.serializer import StoreSerializer

from rest_framework import viewsets


class StoreView(viewsets.ModelViewSet):
    ''' stores view '''
    # permission_code = 'store'
    # queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get_queryset(self):
        params =  self.request.query_params
        star_param = params.get('star', False)
        if star_param:
            return Store.objects.all()[:10]
        return Store.objects.all()
