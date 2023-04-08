from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
    list_display_links = ["reservation", "content"]
    search_fields = ["reservation", "content"]
    list_filter = ["created_date"]

    class Meta:
        model = Comment