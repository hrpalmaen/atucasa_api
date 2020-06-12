''' File branches views '''

from atucasa.models import Branch
from atucasa.serializer import BranchSerializer

from rest_framework import viewsets


class BranchView(viewsets.ModelViewSet):
    '''
    Vista Grupos - django
    '''
    # permission_code = 'branch'
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
