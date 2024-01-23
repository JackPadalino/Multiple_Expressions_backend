from django.contrib import admin
from .models import (Tag, Track, Video)

# Register your models here.
admin.site.register(Tag)
admin.site.register(Track)
admin.site.register(Video)