from django.db import models

# Create your models here.

class Casts(models.Model):
    Name = models.CharField(max_length=200)
    Dob = models.DateField()
    About = models.TextField(max_length=2000)
    Image = models.ImageField(upload_to='Actor', null=True, blank=True)
    Awards = models.IntegerField(null=True, blank=True) # Can be moved to another table
    Nationality = models.CharField(max_length=200)
    ROLE_CHOICES = [
        ('A', 'actor'),
        ('D', 'director'),
        ('P', 'producer'),
        ('O', 'other'),
        ('W', 'writer'),
    ]
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    def __str__(self):
        return self.Name
