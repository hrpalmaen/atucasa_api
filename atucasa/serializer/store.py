''' File stores serializer '''

from rest_framework import serializers

from atucasa.models import Store

class StoreSerializer(serializers.ModelSerializer):
    ''' stores serializer '''

    class Meta:
        model = Store
        fields = ('__all__')
      