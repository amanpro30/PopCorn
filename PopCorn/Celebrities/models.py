from django.db import models


class Celebrity(models.Model):
    Name = models.CharField(max_length=200)
    Dob = models.DateField()
    About = models.TextField(max_length=2000)
    Image = models.ImageField(upload_to='Celebrity', null=True, blank=True)
    Nationality = models.CharField(max_length=200)

    def __str__(self):
        return self.Name


class Award(models.Model):
    Name = models.CharField(max_length=100)
    Date = models.DateField()
    Cast = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
