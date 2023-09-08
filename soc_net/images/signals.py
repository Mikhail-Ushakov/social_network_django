from django.dispatch import receiver
from django.db.models.signals import m2m_changed

from .models import ImageModel


@receiver(m2m_changed, sender=ImageModel.likes.through)
def likes_change(sender, instance, **kwargs):
    instance.total_likes = instance.likes.count()
    instance.save()