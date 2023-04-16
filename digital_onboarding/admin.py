from django.contrib import admin
from .models import TechServiceCandidate


@admin.register(TechServiceCandidate)
class TechServiceCandidateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TechServiceCandidate._meta.fields]
    list_display_links = ["service_name"]
    search_fields = ["service_name"]
    list_filter = ["created_date"]

    class Meta:
        model = TechServiceCandidate