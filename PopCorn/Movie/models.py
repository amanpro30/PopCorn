from django.db import models
from Celebrities.models import Celebrity
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Show(models.Model):
    Title = models.CharField(max_length=200, db_index=True)
    ReleaseDate = models.DateField(db_index=True)
    Duration = models.TimeField()
    Description = models.TextField(max_length=2000)
    Image = models.ImageField(upload_to='Show', default='movie.jpg')
    Country = models.CharField(max_length=200)
    Budget = models.IntegerField()
    Boc = models.IntegerField(db_index=True)
    # STATUS_CHOICE = (
    #     ('F', 'Flop'),
    #     ('A', 'Average'),
    #     ('H', 'Hit'),
    #     ('S', 'SuperHit'),
    #     ('B', 'Blockbuster'),
    #     ('R', 'Running')
    # )
    Status = models.CharField(max_length=1)
    Avg_rating = models.FloatField(db_index=True)
    Num_rating = models.IntegerField(default=0)
    Trailer = models.CharField(max_length=200)
    SHOW_TYPE = (
        ('T', 'TvSeries'),
        ('M', 'Movies'),
    )
    Type = models.CharField(max_length=1, choices=SHOW_TYPE)

    def __str__(self):
        return self.Title


class Genre(models.Model):
    Show = models.ForeignKey(Show, on_delete=models.CASCADE)
    GENRE_CHOICES = (
        ('R', 'Romance'),
        ('C', 'Comedy'),
        ('T', 'Thriller'),
        ('S', 'Sci-Fi'),
        ('D', 'Drama'),
        ('A', 'Action')
    )
    Genre = models.CharField(max_length=1, choices=GENRE_CHOICES)

    def __str__(self):
        return self.Movie_title


class ShowCelebrity(models.Model):
    Show = models.ForeignKey(Show, on_delete=models.CASCADE)
    Celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('A', 'actor'),
        ('D', 'director'),
        ('P', 'producer'),
        ('W', 'writer'),
    ]
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    def __str__(self):
        return self.Show, self.Celebrity


class Season(models.Model):
    Title = models.CharField(max_length=200)
    ReleaseDate = models.DurationField(db_index=True)
    Show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return self.Season_title


class Episode(models.Model):
    Title = models.CharField(max_length=200)
    Duration = models.TimeField()
    Season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.Episode_title


class Rating(models.Model):
    Show = models.ForeignKey(Show, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Stars = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.movie, self.stars


class Review(models.Model):
    Show = models.ForeignKey(Show, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Statement = models.CharField(max_length=5000)
    PostDate = models.DateTimeField(db_index=True, auto_now_add=True)


class Upvote(models.Model):
    Review = models.ForeignKey(Review, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)


class Favourite(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    TYPE_CHOICE = (
        ('F', 'Favourites'),
        ('W', 'Watchlist')
    )
    Type = models.CharField(max_length=1, choices=TYPE_CHOICE)
