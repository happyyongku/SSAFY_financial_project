
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from django.contrib.auth import get_user_model
from .serializers import UserProfileSerializer, UserProfileEditSerializer
# Create your views here.

@api_view(['GET','PUT', 'DELETE'])
def profile(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    if request.method == 'GET':       
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = UserProfileEditSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            print('confirm')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)
