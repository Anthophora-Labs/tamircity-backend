from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from device_types.models import DeviceType
from brands.models import Brand


class TechService(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tech_service')
    #device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, related_name='tech_services')
    #brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='tech_services')
    description = models.TextField(blank=True, null=True, max_length=500)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_prof(sender, instance, created, **kwargs):
    if not created:
        return
    TechService.objects.create(user=instance)
    instance.tech_service.save()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    full_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.user.username