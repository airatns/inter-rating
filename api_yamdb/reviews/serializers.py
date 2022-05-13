from rest_framework import serializers
from rest_framework_nested import serializers as nested_serializers

from .models import Comment, Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class TitleReviewSerializer(
    nested_serializers.NestedHyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
