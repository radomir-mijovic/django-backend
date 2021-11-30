from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView
)
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from knox.models import AuthToken
from knox.serializers import UserSerializer
from .serizlizers import *


class GetAuthUserView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get_object(self):
        return self.request.user


class LoginUserView(APIView):
    permission_classes = [
        AllowAny
    ]

    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            data = {
                'success': 'You are logged in successfully',
                'user': user.username,
                'token': AuthToken.objects.create(user)[1]
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class RegisterUserView(CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = {
                'success': 'Your account is created',
                'user': user.username,
                'token': AuthToken.objects.create(user)[1]
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(UpdateAPIView):
    permission_classes = [
        IsAuthenticated
    ]

    def get_object(self, queryset=None):
        return self.request.user
