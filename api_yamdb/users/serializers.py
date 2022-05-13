from rest_framework import serializers

from users.models import User, CHOICES


# class UserSerializer(serializers.ModelSerializer):
#     role = serializers.ChoiceField(choices=CHOICES, default='user')

#     class Meta:
#         model = User
#         fields = '__all__'


class SignUpSerializer(serializers.ModelSerializer):
    """Сериалайзер на регистрацияю нового пользователя.
    """
    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                'имя "me" является системным и не может быть выбрано'
            )
        return username

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TokenSerializer(serializers.ModelSerializer):
    """Сериалайзер на токен для пользователя.
    """
    class Meta:
        model = User
        fields = ('username', 'confirmation_code',)
