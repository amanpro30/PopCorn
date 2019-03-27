from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from casts.models import Casts
import datetime
# Create your models here.


class MovieSeries(models.Model):
    Movie_title = models.CharField(max_length=200)
    Duration = models.IntegerField()
    Description = models.TextField(max_length=20000)
    ReleaseDate = models.DateField()
    Cast = models.ManyToManyField(Casts, related_name="cast")
    GENRE_CHOICES = (
        ('R', 'Romance'),
        ('C', 'Comedy'),
        ('T', 'Thriller'),
        ('S', 'Sci-Fi'),
        ('D', 'Drama'),
        ('A', 'Action')
    )
    Genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    Country = models.CharField(max_length=200)
    Boc = models.IntegerField()
    STATUS_CHOICE = (
        ('F', 'Flop'),
        ('L', 'Losing'),
        ('A', 'Average'),
        ('H', 'Hit'),
        ('S', 'Superhit'),
        ('B', 'Blockbuster')
    )
    Status = models.CharField(max_length=1, choices=STATUS_CHOICE, null=True, blank=True)
    Trailer = models.CharField(max_length=2000, null=True, blank=True)


class SEASON(models.Model):
    Season_title = models.CharField(max_length=200, null=True, blank=True)
    Series = models.ForeignKey(MovieSeries, on_delete=models.CASCADE, null=True, blank=True)


class EPISODE(models.Model):
    Episode_title = models.CharField(max_length=200, null=True, blank=True)
    Duration = models.IntegerField(null=True, blank=True)
    Season = models.ForeignKey(SEASON, on_delete=models.CASCADE, null=True, blank=True)




