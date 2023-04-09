from django.db import models
from django.contrib.auth.models import User


TechServiceCandidateStatus = (
    ("Pending", "Pending"),
    ("Cancelled", "Cancelled"),
    ("Approved", "Approved"),
)


class TechServiceCandidate(models.Model):
    service_name = models.CharField(max_length=150)
    business_type = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    number_of_branches = models.IntegerField()
    number_of_technicians = models.IntegerField()
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=TechServiceCandidateStatus)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.service_name