from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ImageModel
from .forms import ImageForm

@login_required
def create_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            image = form.save(commit=False)
            image.user = request.user
            image.save()
    else:
        form = ImageForm(request.GET)

    return render(request, 'images/create_image.html', {'section': 'images', 'form': form})
