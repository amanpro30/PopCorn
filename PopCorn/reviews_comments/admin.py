from django.contrib import admin
from .models import Ratings, Upvotes, Review

# Register your models here.

admin.site.register(Ratings)
admin.site.register(Upvotes)
admin.site.register(Review)
