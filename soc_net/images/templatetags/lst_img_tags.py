from django import template
from images.models import ImageModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


register = template.Library()

@register.inclusion_tag('images/list_images_for_tag.html')
def list_images_tag(user=None, page=None):
    if user:
        images = ImageModel.objects.filter(user=user)
    else:
        images = ImageModel.objects.all()
        paginator = Paginator(images, 8)
        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            images = paginator.page(1)
        except EmptyPage:
            images = paginator.page(paginator.num_pages)
    return {'images': images, 'is_user': user}