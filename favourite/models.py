from django.db import models
from django.contrib.auth.models import User


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=120, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.user.username