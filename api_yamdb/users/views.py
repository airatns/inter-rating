import jwt
import os
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.serializers import UserSerializer, TokenSerializer
from users.models import User
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import generics, viewsets
from cryptography.hazmat.primitives import serialization


def create_confirmation_code(username, email):
    """При регистрации генерируется токен и отправляется на email.
    """
    user = get_object_or_404(User, username=username)
    code = default_token_generator.make_token(user)
    send_mail(
        subject='Registration token',
        message=f'Привет {username}. Пожалуйста, используйте этот токен {code}',
        from_email='from@example.com',
        recipient_list=[email],
    )
    user.confirmation_code = code
    user.save()

    return code


# def create_jwt_token(user):
#     payload_data = {
#         'token_type': 'access',
#         'exp': 1665736555,
#         'user_id': user.id,
#     }
#     key_data = 'secret'
#     token = jwt.encode(
#         payload=payload_data,
#         key=key_data,
#         algorithm='HS256'
#     )
#     return token


class SignUp(CreateAPIView):
    """Регистрация нового пользователя.
    """
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        username = serializer.data['username']
        email = serializer.data['email']
        create_confirmation_code(username, email)

        return Response(serializer.data)


class Token(CreateAPIView):
    """Запрос на JWT-токен.
    """
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer

    def post(self, request):
        """Проверяем, корректен ли код подтверждения.
        Если код корректен, выдаем токен.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, username=serializer.data['username'])
        if user.confirmation_code != serializer.data['confirmation_code']:
            return Response('Код подтверждения некорректен')
        token = AccessToken.for_user(user)      # def
        return Response(str(token))


class UserAccountDetail(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    # def get_queryset(self):
    #     new_queryset = User.objects.get(username=self.request.user.username)
    #     return new_queryset

    def get(self, request):
        user = get_object_or_404(User, username=self.request.user.username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

