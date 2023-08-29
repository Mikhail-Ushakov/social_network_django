from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.text import slugify
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
import requests

from .models import ImageModel
from .forms import ImageForm


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
            return HttpResponseRedirect(reverse('detail-image', args=[image.slug]))

    else:
        form = ImageForm(request.GET or None, initial={'url': f'{request.build_absolute_uri()}-{request.user}-default.png'})
        # print(form.data)    
    return render(request, 'images/create_image.html', {'section': 'images', 'form': form})

@login_required
def image_detail(request, slug):
    image = get_object_or_404(ImageModel, slug=slug)
    return render(request, 'images/detail_image.html', {'image': image})

@login_required
@require_POST
def image_like(request, id):
    # id = request.POST.get('id')
    image = get_object_or_404(ImageModel, id=id)
    if request.user in image.likes.all():
        image.likes.remove(request.user)
    else:
        image.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail-image', args=[image.slug]))

@login_required
def image_list(request):
    page = request.GET.get('page')
    return render(request, 'images/list_images.html', {'page': page})