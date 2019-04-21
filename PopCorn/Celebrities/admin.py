from django.contrib import admin
from .models import Celebrity, Award, Tag

# Register your models here.
admin.site.register(Celebrity)
admin.site.register(Award)
admin.site.register(Tag)
