from django.contrib import admin
from .models import NewsLetter


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NewsLetter._meta.fields]
    list_display_links = ["email"]
    search_fields = ["email"]
    list_filter = ["created_date"]

    class Meta:
        model = NewsLetter

