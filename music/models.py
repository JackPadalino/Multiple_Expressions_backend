import os
from django.db import models
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.db.models.signals import post_delete
import boto3 

class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    profile_photo = models.ImageField(upload_to='profile_photos/', default='profile_photos/default.jpeg')
    bio = models.TextField(null=True)

    def __str__(self):
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    artists = models.ManyToManyField(Artist,related_name='tracks')
    description = models.TextField(null=True)
    file = models.FileField(upload_to='tracks/', validators=[FileExtensionValidator(allowed_extensions=['mp3'])],blank=False)
    track_photo = models.ImageField(
        default='track_photos/default.jpeg',
        upload_to='track_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])]
    )
    tags = models.ManyToManyField(Tag,default="Genre")
    upload_date = models.DateTimeField("date uploaded", auto_now_add=True)

    def __str__(self):
        tags_str = ', '.join(tag.title for tag in self.tags.all())
        artists_str = ', '.join(artist.name for artist in self.artists.all())
        return f"{self.title} (Tags: {tags_str}, Artists: {artists_str})"

class Video(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    artists = models.ManyToManyField(Artist,related_name='videos')
    description = models.TextField(null=True)
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
    tags = models.ManyToManyField(Tag,default="Genre")
    upload_date = models.DateTimeField("date uploaded", auto_now_add=True)

    def __str__(self):
        tags_str = ', '.join(tag.title for tag in self.tags.all())
        artists_str = ', '.join(artist.name for artist in self.artists.all())
        return f"{self.title} (Tags: {tags_str}, Artists: {artists_str})"

# delete audio files and images for deleted track from AWS S3 bucket
@receiver(post_delete, sender=Track)
def delete_track_from_s3_bucket(sender, instance, **kwargs):
    aws_key_id = os.environ.get('ME_AWS_ACCESS_KEY_ID')
    aws_secret_key = os.environ.get('ME_AWS_SECRET_ACCESS_KEY')
    aws_bucket_name = os.environ.get('ME_AWS_STORAGE_BUCKET_NAME')

    client = boto3.client('s3', aws_access_key_id=aws_key_id, aws_secret_access_key=aws_secret_key)
    client.delete_object(Bucket=aws_bucket_name, Key=f'{instance.file}')
    client.delete_object(Bucket=aws_bucket_name, Key=f'{instance.track_photo}')

# delete video files and images for deleted track from AWS S3 bucket
@receiver(post_delete, sender=Video)
def delete_video_from_s3_bucket(sender, instance, **kwargs):
    aws_key_id = os.environ.get('ME_AWS_ACCESS_KEY_ID')
    aws_secret_key = os.environ.get('ME_AWS_SECRET_ACCESS_KEY')
    aws_bucket_name = os.environ.get('ME_AWS_STORAGE_BUCKET_NAME')

    client = boto3.client('s3', aws_access_key_id=aws_key_id, aws_secret_access_key=aws_secret_key)
    client.delete_object(Bucket=aws_bucket_name, Key=f'{instance.file}')
    client.delete_object(Bucket=aws_bucket_name, Key=f'{instance.video_photo}')