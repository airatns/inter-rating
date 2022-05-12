from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Genre, Category, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'slug']
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='slug', queryset=Category.objects.all())
    genre = SlugRelatedField(slug_field='slug', many=True, queryset=Genre.objects.all())

    class Meta:
        fields = '__all__'
        read_only_fields = ('rating',)
        model = Title


class TitleListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=False)
    genre = GenreSerializer(many=True)

    class Meta:
        fields = '__all__'
        read_only_fields = ('rating',)
        model = Title
