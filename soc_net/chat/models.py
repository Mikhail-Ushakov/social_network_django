from django.db import models


class ChatModel(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='messeges')
    messege = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    

        
    