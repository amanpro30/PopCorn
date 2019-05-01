from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Show, Season, Episode, ShowCelebrity, Rating, Review, Upvote, Genre, Favourite, Visits

admin.site.register(Show)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(ShowCelebrity)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Upvote)
admin.site.register(Genre)
admin.site.register(Favourite)
admin.site.register(Visits)

