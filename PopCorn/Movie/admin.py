from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import MovieSeries,SEASON,EPISODE

admin.site.register(MovieSeries)
admin.site.register(SEASON)
admin.site.register(EPISODE)