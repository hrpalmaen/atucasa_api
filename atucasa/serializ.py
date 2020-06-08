from rest_framework import serializers
from Api.models import *

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('__all__')

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('__all__')

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ('__all__')