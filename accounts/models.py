from django.db import models
from django.contrib.auth.models import User
import uuid

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='accounts/', null=True, blank=True) 
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0.0) 
    numReviews = models.PositiveIntegerField(null=True, blank=True, default=0)  
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)  
    stock = models.PositiveIntegerField(null=True, blank=True, default=0)  
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name or str(self.uuid)