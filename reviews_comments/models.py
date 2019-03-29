from django.db import models
from django.contrib.auth.models import User
from Movie.models import MovieSeries
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class ratings(models.Model):
    movie = models.ForeignKey(MovieSeries, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )


class comments(models.Model):
    movie = models.ForeignKey(MovieSeries, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class upvotes(models.Model):
    comment = models.ForeignKey(comments, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
