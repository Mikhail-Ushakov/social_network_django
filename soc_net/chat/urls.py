from django.urls import path

from .views import chat_views

urlpatterns = [
    path('', chat_views, name='chat'),
]