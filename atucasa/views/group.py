''' File permissions views '''

from django.contrib.auth.models import Group
from atucasa.serializer import GroupSerializer

from rest_framework import viewsets


class GroupView(viewsets.ModelViewSet):
    ''' categories store view '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
