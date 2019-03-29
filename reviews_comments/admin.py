from django.contrib import admin
from .models import ratings, upvotes, comments

# Register your models here.

admin.site.register(ratings)
admin.site.register(upvotes)
admin.site.register(comments)
