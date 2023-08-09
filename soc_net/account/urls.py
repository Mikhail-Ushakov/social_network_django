from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('logout/', views.AccountLogoutView.as_view(), name='logout'),

    path('', views.dashboard, name='dashboard'),
]