from django.forms import CharField, EmailField
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User, CHOICES


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер на регистрацияю нового пользователя.
    """
    # role = serializers.ChoiceField(choices=CHOICES, default='user')
    username = CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    email = EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio')

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                'имя "me" является системным и не может быть выбрано'
            )
        return username


class TokenSerializer(serializers.ModelSerializer):
    """Сериалайзер на токен для пользователя.
    """
    username = serializers.CharField(required=True,)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code',)


