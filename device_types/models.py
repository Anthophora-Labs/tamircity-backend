from django.db import models


class DeviceType(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name