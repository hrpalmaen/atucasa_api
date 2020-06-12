''' File categories product serializer '''

from rest_framework import serializers

from atucasa.models import Category_Product

class CategoryProductSerializer(serializers.ModelSerializer):
    ''' categories product serializer '''

    class Meta:
        model = Category_Product
        fields = ('__all__')
      