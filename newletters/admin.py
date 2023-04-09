from django.contrib import admin
from .models import NewLetter


@admin.register(NewLetter)
class NewLetterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NewLetter._meta.fields]
    list_display_links = ["email"]
    search_fields = ["email"]
    list_filter = ["created_date"]

    class Meta:
        model = NewLetter

