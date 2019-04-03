from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Show, SEASON, EPISODE, ShowCelebrity, Ratings, Review, Upvotes

admin.site.register(Show)
admin.site.register(SEASON)
admin.site.register(EPISODE)
admin.site.register(ShowCelebrity)
admin.site.register(Ratings)
admin.site.register(Review)
admin.site.register(Upvotes)