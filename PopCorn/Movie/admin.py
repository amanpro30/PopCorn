from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Show, SEASON, EPISODE

admin.site.register(Show)
admin.site.register(SEASON)
admin.site.register(EPISODE)
