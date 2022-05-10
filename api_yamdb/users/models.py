from django.contrib.auth.models import AbstractUser
from django.db import models


CHOICES = (
    ('user', 'пользователь'),
    ('moderator', 'модератор'),
    ('admin', 'администратор'),
)


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роли',
        max_length=16,
        choices=CHOICES,
        default='user',
    )
