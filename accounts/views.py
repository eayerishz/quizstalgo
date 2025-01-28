from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Account
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    user_data = []

    for user in users:
        account = user.account  
        
        user_data.append({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "bio": account.bio,
            "profile_picture": account.profile_picture.url if account.profile_picture else None,
            "phone_number": account.phone_number,
            "address": account.address,
            "createdAt": account.createdAt,
            "updatedAt": account.updatedAt,
        })

    return JsonResponse(user_data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)  
    account = user.account  
    user_data = {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "bio": account.bio,
        "profile_picture": account.profile_picture.url if account.profile_picture else None,
        "phone_number": account.phone_number,
        "address": account.address,
        "createdAt": account.createdAt,
        "updatedAt": account.updatedAt,
    }

    return JsonResponse(user_data, status=status.HTTP_200_OK)
