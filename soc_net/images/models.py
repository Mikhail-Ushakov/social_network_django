from django.conf import settings
from django.db import models
from django.utils.text import slugify

class ImageModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_added', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='image_added/')
    created = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)


    class Meta:
        indexes = [
            models.Index(fields=('-created',))
        ]
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)