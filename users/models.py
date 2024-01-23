from django.db import models
from django.contrib.auth.models import User

# imports for signals
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/', default='profile_photos/default.jpeg')

    def __str__(self):
        return self.user.username

# signals for creating/deleting profiles on creating/deleting users
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(pre_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    try:
        profile = instance.profile
        profile.delete()
    except Profile.DoesNotExist:
        pass