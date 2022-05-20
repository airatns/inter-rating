import datetime as dt

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField("Категории (типы) произведений", max_length=256)
    slug = models.SlugField(unique=True)


class Genre(models.Model):
    name = models.CharField("Жанры произведений", max_length=256)
    slug = models.SlugField(unique=True)


class Title(models.Model):
    name = models.CharField("Имя произведения", max_length=256)
    year = models.IntegerField(
        "Год выпуска",
        validators=[
            MaxValueValidator(dt.datetime.now().year),
            MinValueValidator(1)
        ]
    )
    rating = models.PositiveSmallIntegerField(
        "Рейтинг",
        null=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    description = models.TextField(
        "Описание",
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория'

    )


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              verbose_name='заголовок')
    text = models.TextField(verbose_name='текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='автор')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='дата публикации')
    score = models.IntegerField(verbose_name='Рейтинг',
                                validators=[
                                    MaxValueValidator(10),
                                    MinValueValidator(1)
                                ])

    class Meta:
        unique_together = ('author', 'title',)
        ordering = ['-pub_date']


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               verbose_name='отзыв')
    text = models.TextField(verbose_name='текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='автор')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='дата публикации')

    class Meta:
        ordering = ['-pub_date']
