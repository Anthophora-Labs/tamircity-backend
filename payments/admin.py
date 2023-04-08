from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Payment._meta.fields]
    list_display_links = ["reservation"]
    search_fields = ["reservation", "payment_method"]
    list_filter = ["created_date"]

    class Meta:
        model = Payment