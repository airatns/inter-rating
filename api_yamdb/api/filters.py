import django_filters as filters
from reviews.models import Title


class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name="genre__slug", method='filter_genre')
    category = filters.CharFilter(field_name="category__slug", method='filter_category')
    name = filters.CharFilter(field_name="name", method='filter_name')
    year = filters.CharFilter(field_name="year", method='filter_year')

    class Meta:
        model = Title
        fields = ['genre', 'category', 'year', 'name']

    def filter_genre(self, queryset, name, genre):
        return queryset.filter(genre__slug__contains=genre)

    def filter_category(self, queryset, name, category):
        return queryset.filter(category__slug__contains=category)

    def filter_name(self, queryset, name, value):
        return queryset.filter(name__contains=value)

    def filter_year(self, queryset, name, value):
        return queryset.filter(year__contains=value)
