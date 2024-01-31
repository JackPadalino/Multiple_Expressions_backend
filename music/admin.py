from django.contrib import admin
from .models import (Tag, Artist, Track, Video)

# Register your models here.
admin.site.register(Tag)
admin.site.register(Artist)
admin.site.register(Track)
admin.site.register(Video)