''' products serializer '''

from rest_framework import serializers

from atucasa.models import Product

class ProductSerializer(serializers.ModelSerializer):
    ''' product serializer '''

    class Meta:
        model = Product
        fields = ('__all__')
      