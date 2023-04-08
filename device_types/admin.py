from django.contrib import admin
from .models import DeviceType


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DeviceType._meta.fields]
    list_display_links = ["name", "short_description"]
    search_fields = ["name", "short_description"]
    list_filter = ["created_date"]

    class Meta:
        model = DeviceType