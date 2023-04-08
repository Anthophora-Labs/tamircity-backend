from django.contrib import admin
from .models import Model


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Model._meta.fields]
    list_display_links = ["name"]
    search_fields = ["name"]
    list_filter = ["created_date"]

    class Meta:
        model = Model