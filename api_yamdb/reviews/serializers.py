from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Comment, Review, Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only = True, slug_field = 'username'
    )

    class Meta:
        model = Review
        exclude = ['title']
        extra_kwargs = {
            'title': {'write_only': True}
        }

    def validate(self, attrs):
        author = self.context['request'].user
        title_pk = self.context["view"].kwargs['title_pk']
        title = get_object_or_404(Title, pk = title_pk)
        if (len(Review.objects.filter(title = title, author = author)) > 0
                and self.context["view"].action == "create"):
            raise serializers.ValidationError("Only one review for "
                                              "a title per author")
        return attrs

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        view = self.context.get('view')
        title_pk = view.kwargs['title_pk'] if view else None
        validated_data['title'] = get_object_or_404(Title, pk = title_pk)
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only = True, slug_field = 'username'
    )

    class Meta:
        model = Comment
        exclude = ['review']
        extra_kwargs = {
            'review': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        view = self.context.get('view')
        title_pk = view.kwargs['title_pk'] if view else None
        get_object_or_404(Title, pk = title_pk)
        review_pk = view.kwargs['review_pk'] if view else None
        validated_data['review'] = get_object_or_404(Review, pk = review_pk)
        return super().create(validated_data)
