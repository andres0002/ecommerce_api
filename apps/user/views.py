from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from apps.user.api.serializers import UserTokenSerializer
from apps.user.authentication_mixins import AuthenticationMixin

class UserToken(AuthenticationMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            user_token = Token.objects.get(user=self.user)
            user = UserTokenSerializer(self.user)
            return Response({
                'token':user_token.key,
                'user':user.data
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'error':'Credentials send are incorrect.'
            }, status=status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                print('yeat.')
                if created:
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data,
                        'message':'Successful login.'
                        }, status=status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data['_auth_user_id']):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data,
                        'message':'Successful login.'
                        }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'error':'This user not can start session.'
                    }, status=status.HTTP_401_UNAUTHORIZED)
        return Response({
            'error':'Username or password incorrect.'
            }, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = Token.objects.filter(key=request.POST['token']).first()
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data['_auth_user_id']):
                            session.delete()
                token.delete()
                return Response({
                    'token_message':'Token deleted.',
                    'session_message':'Sessions of user deleted.'
                    }, status=status.HTTP_200_OK)
            return Response({
                'error':'Not be find a user with this credential.'
                }, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({
                'error':'Not be find the token in request.'
                }, status=status.HTTP_409_CONFLICT)
