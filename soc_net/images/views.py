from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.text import slugify
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST

import requests
import redis

from .models import ImageModel
from .forms import ImageForm
from actions.utils import create_action


redis_client = redis.Redis()

@login_required
def create_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        # print(form.fields['url'].to_python()
        # = f'{request.user}_default.png'
        # if request.FILES:
        if form.is_valid():
            # cd = form.cleaned_data
            image = form.save(commit=False)
            image.user = request.user
                # image.url = f'{request.user}_default.png'
            if not request.FILES:
                url_image = form.cleaned_data['url']
                extension = url_image.rsplit('.', 1)[1].lower()
                name_image = slugify(image.title)
                full_name = f'{name_image}.{extension}'
                response = requests.get(url_image)
                image.image.save(full_name, ContentFile(response.content), save=False)
            
            image.save()
            create_action(request.user, 'add image', image)
            return HttpResponseRedirect(reverse('detail-image', args=[image.slug]))

    else:
        form = ImageForm(request.GET or None, initial={'url': f'{request.build_absolute_uri()}-{request.user}-default.png'})
        # print(form.data)    
    return render(request, 'images/create_image.html', {'section': 'images', 'form': form})

@login_required
def image_detail(request, slug):
    image = get_object_or_404(ImageModel, slug=slug)
    total_views = redis_client.incr(f'image:{image.id}')
    redis_client.zincrby('image:rank', 1, image.id)
    return render(request, 'images/detail_image.html', {'image': image, 'total_views': total_views})

@login_required
@require_POST
def image_like(request, id):
    # id = request.POST.get('id')
    image = get_object_or_404(ImageModel, id=id)
    if request.user in image.likes.all():
        image.likes.remove(request.user)
    else:
        image.likes.add(request.user)
        create_action(request.user, 'likes', image)
    return HttpResponseRedirect(reverse('detail-image', args=[image.slug]))

@login_required
def image_list(request):
    page = request.GET.get('page')
    most_populate_id = redis_client.zrange('image:rank', 0, -1, desc=True)[0]
    most_populate_obj = ImageModel.objects.filter(id=most_populate_id)[0]
    return render(request, 'images/list_images.html', {'page': page, 'most_populate_obj': most_populate_obj})