import datetime as dt

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


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
    rating = models.IntegerField(
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
