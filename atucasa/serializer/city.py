''' File cities serializer '''

from rest_framework import serializers

from atucasa.models import City

class CitySerializer(serializers.ModelSerializer):
    ''' cities serializer '''

    class Meta:
        model = City
        fields = ('__all__')
      