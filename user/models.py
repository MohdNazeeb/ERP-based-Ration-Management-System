from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class CustomUser(AbstractUser):
    username = None  # correct
    card_type = models.CharField(max_length=20)
    full_name = models.CharField(max_length=30)
    card_number = models.CharField(max_length=20, unique=True)
    mobile_number = models.CharField(max_length=10)
    shop_id = models.CharField(max_length=20,blank=True,null=True)  # Link to distributor
    image = models.ImageField(upload_to="users/", blank=True, null=True)
    
    USERNAME_FIELD = 'card_number'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return f"{self.full_name} ({self.card_number})"
