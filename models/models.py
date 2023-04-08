from django.db import models
from brands.models import Brand
from device_types.models import DeviceType


class Model(models.Model):
    name = models.CharField(max_length=150)
    short_description = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, related_name='models')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name