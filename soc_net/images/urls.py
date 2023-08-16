from django.urls import path
from . import views

urlpatterns = [
    path('create-image/', views.create_image, name='create-image'),
]