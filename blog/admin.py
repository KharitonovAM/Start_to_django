from django.contrib import admin

from .models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "preview",
        "create_data",
        "is_publicated",
        "number_shows",
    )
