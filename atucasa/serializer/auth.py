''' File for serializer autentication '''

from atucasa.models import User
from rest_framework import serializers

class AuthSerializer(serializers.ModelSerializer):
    ''' autentication serializer '''

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate_username(self, value):
        # print('value username: ', value)
        if value == '' or value == None:
            raise serializers.ValidationError('Este campo es obligatorio.')
        return value
    
    def validate_password(self, value):
        # print('valuepassseorddddddd: ', data.get('password'))
        if value == '' or value == None:
            raise serializers.ValidationError('Este campo es obligatorio.')
        return value
