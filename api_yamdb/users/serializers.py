from django.forms import CharField, EmailField

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User, CHOICES


class SignUpSerializer(serializers.ModelSerializer):
    """Сериалайзер для регистрации пользователя.
    """
    username = CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        read_only_fields = ('role',)

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                'имя "me" является системным и не может быть выбрано'
            )
        return username


class TokenSerializer(serializers.Serializer):
    """Сериалайзер на выдачу токена.
    """
    username = serializers.CharField(
        required=True,
        max_length=150
    )
    confirmation_code = serializers.CharField(
        required=True,
        max_length=256
    )


class MeSerializer(serializers.ModelSerializer):
    """Сериалайзер для редактирвоания своих данных пользователем.
    """
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        read_only_fields = ('username', 'email', 'role',)


class AdminSerializer(serializers.ModelSerializer):
    """Сериалайзер для Администратора.
    """
    role = serializers.ChoiceField(choices=CHOICES, default='user')
    username = CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                'имя "me" является системным и не может быть выбрано'
            )
        return username
