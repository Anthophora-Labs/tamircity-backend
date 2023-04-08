from django.db import models
from device_types.models import DeviceType


class Brand(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, related_name='device_type')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name