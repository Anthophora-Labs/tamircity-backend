from django.contrib import admin
from .models import ExpertiseTV


@admin.register(ExpertiseTV)
class ExpertiseTVdAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExpertiseTV._meta.fields]
    list_display_links = ["reservation"]
    search_fields = ["reservation"]
    list_filter = ["created_date"]

    class Meta:
        model = ExpertiseTV