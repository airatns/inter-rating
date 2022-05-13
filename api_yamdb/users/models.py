# import jwt

# from datetime import datetime, timedelta
# from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


CHOICES = (
    ('user', 'пользователь'),
    ('moderator', 'модератор'),
    ('admin', 'администратор'),
)


class UserManager(BaseUserManager):
    """ Django требует, чтобы при создании нестандартной модели User
    исплользовался свой собственный класс Manager.
    Все, что нам остается сделать - переопределить функцию create_user(),
    которую мы будем использовать для создания объектов User.
    """
    def create_user(self, username, email, password=None, role='úser', bio=None):
        """Метод создает и возвращает модель User
        с электронной почтой и именем пользователя.
        """
        if username is None:
            raise TypeError('User must have a username.')
        if email is None:
            raise TypeError('User must have an email address.')
        user = self.model(username=username, email=self.normalize_email(email))
        user.role = role
        user.bio = bio
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, role='admin', bio = None):
        """Метод создает и возвращает модель User с правами суперпользователя.
        """
        if password is None:
            raise TypeError('Suoeruser must have a password')
        user = self.create_user(username, email, password)
        user.role = role
        user.bio = bio
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    username = models.CharField(
        'Логин',
        db_index=True,
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        'Адрес эдектронной почты',
        db_index=True,
        max_length=254,
        unique=True
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True,
        null=True
    )
    bio = models.TextField(
        'Биография',
        blank=True,
        null=True
    )
    role = models.CharField(
        'Роли',
        max_length=16,
        choices=CHOICES,
        default='user'
    )
    confirmation_code = models.CharField(
        'Токен',
        max_length=256,
        blank=True,
        null=True
    )

    REQUIRED_FIELDS = ['email']

    objects = UserManager()
    """Сообщаем Django, что для работы с объектами этого типа нужно использовать
    определенный выше класс UserManager.
    """

    def __str__(self):
        """Метод возвращает строковое представление текущего User.
        Эта строка используется при выводе модели User в консоли.
        """
        return self.username
