''' File branch serializer '''

from rest_framework import serializers

from atucasa.models import Branch

class BranchSerializer(serializers.ModelSerializer):
    ''' branch serializer '''

    class Meta:
        model = Branch
        fields = ('__all__')
      