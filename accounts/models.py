from django.db import models
from django.contrib.auth.models import User
import uuid

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    first_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_active = models.BooleanField(default=True) 
    createdAt = models.DateTimeField(auto_now_add=True)  
    updatedAt = models.DateTimeField(auto_now=True) 
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) 

    def __str__(self):
        return f'{self.user.username} Account'

    class Meta:
        ordering = ['-createdAt']  