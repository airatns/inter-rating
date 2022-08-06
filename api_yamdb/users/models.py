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
    def create_user(self, username, email, password, **extra_fields):
        """Метод создает и возвращает модель User
        с электронной почтой и именем пользователя.
        """
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            password=password,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, username, email, password, role='admin', **extra_fields
    ):
        """Метод создает и возвращает модель User с правами суперпользователя.
        """
        user = self.create_user(username, email, password, **extra_fields)
        user.role = 'admin'
        user.is_superuser = True
        user.is_staff = True
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
        'Код подтверждения',
        max_length=256,
        default='random'
    )
    is_admin = models.BooleanField()

    objects = UserManager()
    """Сообщаем Django, что для работы с объектами этого типа нужно использовать
    определенный выше класс UserManager.
    """

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        """Метод возвращает строковое представление текущего User.
        Эта строка используется при выводе модели User в консоли.
        """
        return self.username

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'
