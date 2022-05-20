from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from reviews.models import Genre, Category, Title, Review, Comment
from reviews.serializers import ReviewSerializer, CommentSerializer

from .filters import TitleFilter
from .permissions import AdminOrReadOnly, IsObjectOwner
from .serializers import GenreSerializer, CategorySerializer, \
    TitleSerializer, TitleListSerializer


class CreateListDestroyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    pass


class GenresViewSet(CreateListDestroyViewSet):
    queryset = Genre.objects.get_queryset().order_by('id')
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    permission_classes = (AdminOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class CategoriesViewSet(CreateListDestroyViewSet):
    queryset = Category.objects.get_queryset().order_by('id')
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = (AdminOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.get_queryset().order_by('id')
    serializer_class = TitleSerializer
    permission_classes = (AdminOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TitleListSerializer
        return TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsObjectOwner,)

    def get_queryset(self):
        return Review.objects.filter(title_id=self.kwargs['title_pk'])

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs['title_pk'])
        if serializer.is_valid():
            serializer.save(author=self.request.user, title=title)
        return super().perform_create(serializer)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsObjectOwner,)

    def get_queryset(self):
        return Comment.objects.filter(review_id=self.kwargs['review_pk'],
                                      review__title_id=self.kwargs[
                                          'title_pk'])

    def perform_create(self, serializer):
        get_object_or_404(Title, pk=self.kwargs['title_pk'])
        review = get_object_or_404(Review, pk=self.kwargs['review_pk'])
        if serializer.is_valid():
            serializer.save(review=review, author=self.request.user)
        return super().perform_create(serializer)
