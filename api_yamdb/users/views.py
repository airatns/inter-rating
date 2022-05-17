from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from rest_framework import filters, status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from users.models import User
from users.permissions import IsAdmin
from users.serializers import AdminSerializer, MeSerializer
from users.serializers import SignUpSerializer, TokenSerializer


def create_confirmation_code(username, email):
    """Метод генерации кода подтверждения и отправки его на email.
    """
    user = get_object_or_404(User, username=username)
    code = default_token_generator.make_token(user)
    send_mail(
        subject='Registration token',
        message=f'Привет {username}. Вот твой токен {code}',
        from_email='from@example.com',
        recipient_list=[email],
    )
    user.confirmation_code = code
    user.save()
    return code


class SignUp(CreateAPIView):
    """Регистрация нового пользователя.
    """
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    def post(self, request):
        """После заполнения обязательных полей создается новый пользователь
        и генерируется код подтверждения.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        username = serializer.data['username']
        email = serializer.data['email']
        create_confirmation_code(username, email)

        return Response(
            {'email': email,
             'username': username},
            status=status.HTTP_200_OK)


class Token(CreateAPIView):
    """Создание JWT-токена.
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
            return Response(
                'Код подтверждения некорректен',
                status=status.HTTP_400_BAD_REQUEST
            )
        token = AccessToken.for_user(user)
        return Response(str(token))


class UserAccountDetail(APIView):
    """Просмотр и редактирование данных аккаунта пользователя.
    Функционал пользователя.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = MeSerializer

    def get(self, request):
        user = get_object_or_404(User, username=self.request.user.username)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def patch(self, request):
        user = get_object_or_404(User, username=self.request.user.username)
        serializer = self.serializer_class(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    """Просмотр, редактирование данных аккаунта пользователя.
    Добавление и удаление пользователя.
    Функционал администратора.
    """
    queryset = User.objects.get_queryset().order_by('id')
    serializer_class = AdminSerializer
    permission_classes = (IsAuthenticated, IsAdmin)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'
