from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class Tag(models.Model):
    TAG_CHOICES = (
        ("Techno", "Techno"),
        ("Hardgroove", "Hardgroove"),
        ("Disco", "Disco"),
        ("Nu-Disco", "Nu-Disco"),
        ("Funk", "Funk"),
        ("House", "House"),
    )
    title = models.CharField(max_length=255, choices=TAG_CHOICES, unique=True)

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    profile_photo = models.ImageField(upload_to='profile_photos/', default='profile_photos/default.jpeg')
    bio = models.TextField(default='')

    def __str__(self):
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    artists = models.ManyToManyField(Artist,related_name='tracks')
    file = models.FileField(upload_to='tracks/', validators=[FileExtensionValidator(allowed_extensions=['mp3'])],blank=False)
    track_photo = models.ImageField(
        default='track_photos/default.jpeg',
        upload_to='track_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])]
    )
    tags = models.ManyToManyField(Tag)
    upload_date = models.DateTimeField("date uploaded", auto_now_add=True)

    def __str__(self):
        tags_str = ', '.join(tag.title for tag in self.tags.all())
        artists_str = ', '.join(artist.name for artist in self.artists.all())
        return f"{self.title} (Tags: {tags_str}, Users: {artists_str})"

class Video(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    artists = models.ManyToManyField(Artist,related_name='videos')
    file = models.FileField(
        upload_to='videos/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'avi', 'mov'])],
        blank=False
    )
    video_photo = models.ImageField(
        default='video_photos/default.jpeg',
        upload_to='video_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])]
    )
    tags = models.ManyToManyField(Tag)
    upload_date = models.DateTimeField("date uploaded", auto_now_add=True)

    def __str__(self):
        tags_str = ', '.join(tag.title for tag in self.tags.all())
        artists_str = ', '.join(artist.name for artist in self.artists.all())
        return f"{self.title} (Tags: {tags_str}, Users: {artists_str})"