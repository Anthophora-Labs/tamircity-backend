from django.contrib import admin
from .models import ServiceType


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ServiceType._meta.fields]
    list_display_links = ["name"]
    search_fields = ["name", "price"]
    list_filter = ["created_date"]

    class Meta:
        model = ServiceType
