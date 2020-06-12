''' File categories store serializer '''

from rest_framework import serializers

from atucasa.models import Category_Store

class CategoryStoreSerializer(serializers.ModelSerializer):
    ''' stores serializer '''

    class Meta:
        model = Category_Store
        fields = ('__all__')
      