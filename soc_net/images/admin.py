from django.contrib import admin
from .models import ImageModel


@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'image', 'created']
    list_filter = ['created']