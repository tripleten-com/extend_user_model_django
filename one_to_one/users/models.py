from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class Profile(models.Model):
    # Create a relationship with the default user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(
        'Bio',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Additional field'
        verbose_name_plural = 'Additional fields'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
