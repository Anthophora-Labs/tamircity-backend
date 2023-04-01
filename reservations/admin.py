from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reservation._meta.fields]
    list_display_links = ["full_name", "email"]
    search_fields = ["full_name", "email"]
    list_filter = ["created_date"]

    class Meta:
        model = Reservation