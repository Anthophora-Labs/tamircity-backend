from django.contrib import admin
from .models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Brand._meta.fields]
    list_display_links = ["name"]
    search_fields = ["name"]
    list_filter = ["created_date"]

    class Meta:
        model = Brand