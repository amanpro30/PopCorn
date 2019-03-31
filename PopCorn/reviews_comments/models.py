from django.db import models
from django.contrib.auth.models import User
from Movie.models import MovieSeries
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Ratings(models.Model):
    movie = models.ForeignKey(MovieSeries, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )


class Review(models.Model):
    movie = models.ForeignKey(MovieSeries, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_statement = models.CharField(max_length=1000)


class Upvotes(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
