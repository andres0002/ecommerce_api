from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.user.models import User
from apps.user.api.serializers import UserSerializer, UserListSerializer

@api_view(['GET', 'POST'])
def user_api_view(request, *args, **kwargs):
    model = User
    if request.method == 'GET':
        users = model.objects.all().values('id', 'username', 'name', 'lastname', 'email')
        users_serializer = UserListSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk):
    model = User
    user = model.objects.filter(id=pk).first()
    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'User delete successfully!'}, status=status.HTTP_200_OK)
    else:
        return Response({'message':'User not exist.'}, status=status.HTTP_400_BAD_REQUEST)