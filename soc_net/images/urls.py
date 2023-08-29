from django.urls import path
from . import views

urlpatterns = [
    path('create-image/', views.create_image, name='create-image'),
    path('detail-image/<slug:slug>/', views.image_detail, name='detail-image'),
    path('list-images/', views.image_list, name='list-images'),
    path('like-image/<int:id>/', views.image_like, name='like-image'),
]