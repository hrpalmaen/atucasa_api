''' File for users view '''
from atucasa.models import User
from atucasa.serializer import UserSerializer
from django.contrib.auth.models import Group
# from ..filters import userFilter

from django.conf import settings
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets

class UserView(viewsets.ModelViewSet):
  ''' user or client view '''

#   permission_code = 'user'
  queryset = User.objects.all()
  serializer_class = UserSerializer
#   filter_class = userFilter

#   def create(self, request):
#     ''' create user method '''
#     data = request.data
#     # password = generatePassword(self)
#     groups_data = data.pop('groups')
    
#     try:
#       user_current = User.objects.get(username=data['username'])
      
#       return Response({'detail': ['El usuario ya se encuentra registrado']}, status=404)
#     except:
#       pass    

#     try:
#       # validate existent for group
#       group = Group.objects.filter(id__in=groups_data)

#       user = User.objects.create_user(
#         username = data['username'],
#         first_name = data['first_name'],
#         last_name =  data['last_name'],
#         email = data['email'],
#         is_active = data['is_active'],
#         contact_phone = data['contact_phone'],
#         type_identification = 'CC',
#         identification = data['identification']
#       )
#       user.set_password(password)
#       user.groups.set(groups_data)
#       user.save()

#       return Response(data, status=200)
     
#     except Exception as e:
#       return Response({'detail': ['se han presentado la siguiente excepcion ' + e]}, status=404)

  