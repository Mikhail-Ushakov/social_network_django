from django.forms import ModelForm
from .models import ChatModel
class ChatForm(ModelForm):

    class Meta:
        model = ChatModel
        fields = ['messege']