from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import datetime as dt


class Categories(models.Model):
    name = models.CharField("Категории (типы) произведений", max_length=256)
    slug = models.SlugField(unique=True)


class Genres(models.Model):
    name = models.CharField("Жанры произведений", max_length=256)
    slug = models.SlugField(unique=True)


class Titles(models.Model):
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
        validators=[
           MaxValueValidator(10),
           MinValueValidator(1)
        ]
    )
    description = models.TextField
    genre = models.ManyToManyField(
        Genres,
        # on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория'

    )

# Create your models here.
