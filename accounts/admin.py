from django.contrib import admin
from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    list_display_links = ["user"]
    search_fields = ["user"]
    list_filter = ["created_date"]

    class Meta:
        model = Profile