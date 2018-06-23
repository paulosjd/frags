from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from compounds.models import Compound


class Profile(models.Model):
    """
    A model representing a User and their activity
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username + '_profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates an instance when a User instance is created
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Updates an instance when a User instance is updated
    """
    instance.profile.save()


# class Activity(models.Model):
#     ACTIVITY_TYPES = (
#         (1, 'Compound notes'),
#     )
#     user = models.ForeignKey(
#         Profile,
#         on_delete=models.CASCADE
#     )
#     activity_type = models.IntegerField(choices=ACTIVITY_TYPES)
#
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey()