from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from reservations.models import Reservation


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='reservation')
    content = models.TextField(max_length=500)
    #parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        return f"{self.reservation.full_name} {self.user.username}"

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.created = timezone.now()
    #     self.modified = timezone.now()
    #     return super(Comment, self).save(*args, **kwargs)

    # def children(self):
    #     return Comment.objects.filter(parent=self)
    #
    # @property
    # def any_children(self):
    #     return Comment.objects.filter(parent = self).exists()