''' File cities views '''

from atucasa.models import City
from atucasa.serializer import CitySerializer

from rest_framework import viewsets


class CityView(viewsets.ModelViewSet):
    ''' cities view '''
    # permission_code = 'city'
    queryset = City.objects.all()
    serializer_class = CitySerializer
