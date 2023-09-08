from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Action(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='actions')
    verb = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    target_cont_type = models.ForeignKey(ContentType, 
                                         blank=True, 
                                         null=True, 
                                         on_delete=models.CASCADE,
                                         related_name='target_obj')
    target_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_cont_type', 'target_id')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=('-created',)),
            models.Index(fields=('target_cont_type', 'target_id')),
        ]