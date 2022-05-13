import os
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.serializers import SignUpSerializer, TokenSerializer
from users.models import User
from rest_framework_simplejwt.settings import api_settings


def create_confirmation_code(username, email):
    """При регистрации генерируется токен и отправляется на email.
    """
    user = get_object_or_404(User, username=username)
    code = default_token_generator.make_token(user)
    send_mail(
        subject='Registration token',
        message=f'Пожалуйста, используйте этот токен {code}',
        from_email='from@example.com',
        recipient_list=[email],
    )
    user.confirmation_code = code
    user.save()

    return code


class SignUpView(CreateAPIView):
    """Регистрация нового пользователя.
    """
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        username = serializer.data['username']
        email = serializer.data['email']
        create_confirmation_code(username, email)

        return Response(serializer.data)


# def create_jwt_token(user):
#     payload_data = {
#         'sub': 'user.id',
#         'nickname': 'user.username',
#         'role': 'user.role',
#     }
#     secret = os.environ['SECRET_KEY']

# class TokenView(CreateAPIView):
#     """Запрос на JWT-токен.
#     """
#     permission_classes = (AllowAny,)
#     serializer_class = TokenSerializer

#     def check_token(self, username, code):
#         """Проверяем, корректен ли код подтверждения.
#         Если код корректен, выдаем токен.
#         """
#         user = get_object_or_404(User, username=username)
#         if user.confirmation_code==code:
#             token = create_jwt_token(user)
#             return token
#         return Response('Код подтверждения некорректен')

        
    
    
#     def create(self, request):
#         user = get_object_or_404(User, username=request.user)
#         if user is not None and default_token_generator.check_token(user, code):
#             serializer = self.serializer_class(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response('Токен для ваших запросов: {}'.format(token))



    # def get_token(username, token):
    #     user = get_object_or_404(User, username=username)
    #     if user is not None and default_token_generator.check_token(user, token):
    #         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    #         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    #         payload = jwt_payload_handler(user)
    #         token = jwt_encode_handler(payload)
    #         return Response('Токен для ваших запросов: {}'.format(token))
