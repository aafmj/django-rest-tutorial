from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import UserSerializer
from .permissions import IsOwner


@api_view(['POST'])
@permission_classes((AllowAny, ))
def create_user(request):
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    # first_name = request.data['first_name']
    # last_name = request.data['last_name']
    # username = request.data['username']
    # email = request.data['email']
    # password = request.data['password']
    # print(first_name, last_name, password)
    # return Response(request.user, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes((IsAuthenticated, IsOwner))
def profile(request):
    try:
        user = User.objects.get(username=request.user.username)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ser = UserSerializer(user)
    return Response(ser.data, status=status.HTTP_200_OK)












