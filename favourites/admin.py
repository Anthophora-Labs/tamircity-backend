from django.contrib import admin
from favourites.models import Favourite


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Favourite._meta.fields]
    list_display_links = ["user", "fav_user"]
    search_fields = ["user", "fav_user"]
    list_filter = ["created_date"]

    class Meta:
        model = Favourite