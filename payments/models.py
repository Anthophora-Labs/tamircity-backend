from django.db import models
from reservations.models import Reservation


PAYMENT_TYPE = (
    ('Card', 'Kart'),
    ('Cash', 'Nakit'),
)


class Payment(models.Model):
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=30, choices=PAYMENT_TYPE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='payments')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)