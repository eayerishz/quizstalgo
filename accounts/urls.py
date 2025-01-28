from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.get_users, name='get_account'),
    path('account/<uuid:user_uuid>/', views.get_user, name='get_account'),
]
