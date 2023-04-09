from django.contrib import admin
from accounts.models import TechService


@admin.register(TechService)
class TechServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TechService._meta.fields]
    list_display_links = ["user"]
    search_fields = ["user"]
    list_filter = ["created_date"]

    class Meta:
        model = TechService