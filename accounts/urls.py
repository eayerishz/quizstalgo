from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_users'),
    path('users/<uuid:user_uuid>/', views.get_user, name='get_user'),
]
