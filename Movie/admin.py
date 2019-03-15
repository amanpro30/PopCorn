from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Movie,TVseries,Actor,SEASON,EPISODE

admin.site.register(Movie)
admin.site.register(TVseries)
admin.site.register(Actor)
admin.site.register(SEASON)
admin.site.register(EPISODE)