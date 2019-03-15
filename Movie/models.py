from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
import datetime
# Create your models here.



class Actor(models.Model):
    Actor=models.CharField(max_length=200)
    Dob=models.DateField()
    About=models.TextField(max_length=2000)
    Image=models.ImageField(upload_to='Actor',null=True,blank=True)
    Awards=models.IntegerField(null=True,blank=True)
    Nationality=models.CharField(max_length=200)

class Movie(models.Model):
    Movie=models.CharField(max_length=200)
    Duration=models.IntegerField()
    Description=models.TextField(max_length=20000)
    ReleaseDate = models.DateField()
    Cast = models.ManyToManyField(Actor, related_name="cast")
    Director=models.CharField(max_length=200)
    Writer=models.CharField(max_length=200)
    GENRE = (
        ('R', 'Romance'),
        ('C', 'Comedy'),
        ('T', 'Thriller'),
        ('S','Sci-Fi'),
        ('D','Drama'),
        ('A','Action')
    )
    Genre = models.CharField(max_length=1, choices=GENRE)
    Country=models.CharField(max_length=200)
    Boc=models.IntegerField()
    STATUS = (
        ('F', 'Flop'),
        ('L', 'Losing'),
        ('A', 'Average'),
        ('H', 'Hit'),
        ('S', 'Superhit'),
        ('B', 'Blockbuster')
    )
    Status = models.CharField(max_length=1, choices=STATUS,null=True,blank=True)
    Trailer=models.CharField(max_length=2000,null=True,blank=True)



class TVseries(models.Model):
    Series= models.CharField(max_length=200)
    Description = models.TextField(max_length=20000)
    ReleaseDate = models.DateField()
    Cast = models.ManyToManyField(Actor, related_name="Starcast")
    Director = models.CharField(max_length=200)
    Writer = models.CharField(max_length=200)
    GENRE = (
        ('R', 'Romance'),
        ('C', 'Comedy'),
        ('T', 'Thriller'),
        ('S', 'Sci-Fi'),
        ('D', 'Drama'),
        ('A', 'Action')
    )
    Genre = models.CharField(max_length=1, choices=GENRE)
    Country = models.CharField(max_length=200)
    Trailer = models.CharField(max_length=2000, null=True, blank=True)



class SEASON(models.Model):
    Season=models.CharField(max_length=200,null=True,blank=True)
    Series=models.ForeignKey(TVseries,on_delete=models.PROTECT,null=True,blank=True)



class EPISODE(models.Model):
    Episode=models.CharField(max_length=200,null=True,blank=True)
    Duration=models.IntegerField(null=True,blank=True)
    Season=models.ForeignKey(SEASON,on_delete=models.PROTECT,null=True,blank=True)




