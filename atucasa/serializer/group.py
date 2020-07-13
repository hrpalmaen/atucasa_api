''' File permissions user serializer '''

from rest_framework import serializers

from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):
    ''' groups serializer '''

    class Meta:
        model = Group
        fields = ('id', 'name')
      