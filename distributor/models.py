from django.db import models
from django.conf import settings
from user.models import *

class Distributor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='distributor_profile'  
    )
    full_name = models.CharField(max_length=30)  # ok, optional duplicate
    shop_id = models.CharField(max_length=20, unique=True)
    shop_name = models.CharField(max_length=100)
    shop_address = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    image = models.ImageField(upload_to='distributors/', blank=True, null=True)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField()
    area_assigned = models.CharField(max_length=100, blank=True, null=True)
    # REMOVE password field — distributor password comes from linked CustomUser
    # password = models.CharField()  # ❌ remove this

    def __str__(self):
        return f"{self.shop_name} ({self.user.full_name})"
    


class DistributorSettings(models.Model):
    distributor = models.OneToOneField(Distributor, on_delete=models.CASCADE)

    distribution_from = models.DateField(null=True, blank=True)
    distribution_to = models.DateField(null=True, blank=True)

    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    slot_limit = models.IntegerField(default=0)

    biometric_status = models.CharField(max_length=10, default="ACTIVE")

    def __str__(self):
        return f"{self.distributor.shop_id} Settings"
    
class Announcement(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:20]}..."



#Jatin ->
class BiometricStatus(models.Model):
    device_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"{self.device_id} - {self.status}"
