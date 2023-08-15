from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users_photo/', blank=True)

    def __str__(self) -> str:
        return f'Profile of {self.user.username}'