''' File for authentication '''

from rest_framework.views import APIView
from atucasa.serializer import AuthSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings

class AuthView(APIView):
    ''' Method for authentication '''
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        ''' autenticate method '''
        
        data = request.data
        serializer_auth = AuthSerializer(data=data, many=False)

        # if not serializer_auth.is_valid():
        #     return Response(serializer_auth.errors, status=400)
        
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = authenticate(username=username, password=password)
            groups = user.groups.values_list('name',flat = True)

            if user is not None:
                try:
                    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)
                    return Response({'first_name': user.first_name, 'last_name': user.last_name, 'admin': user.is_superuser, 'username': user.username, 'groups': list(groups), 'token': token}, status=202)
                except Exception as e:
                    return Response({'detail': 'Acceso denegado: ' + str(e)}, status=401)
            else:
                return Response({'detail': 'Las credenciales no son correctas.'}, status=404)
            
        except:
            return Response({'detail': 'El usuario no cuenta con un  perfil activo.'}, status=401)



