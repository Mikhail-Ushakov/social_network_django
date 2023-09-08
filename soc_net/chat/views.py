from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import ChatModel
from .forms import ChatForm

@login_required
def chat_views(request):
    form = ChatForm(request.POST or None)
    messeges = ChatModel.objects.all()
    if request.method == 'POST':
        msg = form.save(commit=False)
        msg.user = request.user
        msg.save()
        return HttpResponseRedirect(reverse('chat'))
    return render(request, 'chat/chat.html', {'messeges': messeges, 'form': form})