from django.contrib import admin
from .models import ratings, upvotes, review

# Register your models here.

admin.site.register(ratings)
admin.site.register(upvotes)
admin.site.register(review)
